from src.helper.mapping import Mapping
from src.helper.get_data import GetData
from src.helper.save_json import SaveJson
from src.exception.exception import SaveJsonError, UploadS3Error
from src.s3.uploadS3 import upload_to_s3

async def process_data(url):
    print(url)

    urls_csv = await GetData.detect_csv_requests(url)
    for url_csv in urls_csv:
        
        tahun, kategori, filename = await GetData.save_csv(url_csv)
        print(f'Downloaded {filename} for {kategori} in {tahun}')

        path = f'csv/{kategori}/{tahun}/{filename}'
        data_reader = Mapping(filename)
        data = await data_reader.read_csv(path)

        for item in data:
            name = item['name'].replace(' ','_').lower()
            year = item['year']


            filename_json = f'{name}_{year}.json'

            local_path = f'data/{kategori.replace(" ", "_").lower()}/{tahun}/json/{filename_json.lower().replace(" ","_")}'
            s3_path = f's3://ai-pipeline-raw-data/data/data_statistics/visionofhumanity/{kategori.replace(" ","_").lower()}/{tahun}/json/{filename_json.lower()}'

            try:
                dj = SaveJson(response=url_csv, s3_path=s3_path, data=item, tahun=tahun, tag=kategori)
                await dj.save_json_local(kategori, filename_json, tahun)
                print(f'Successfully saved JSON for {filename_json}')
            except SaveJsonError as e:
                await e.send_message()
            except Exception as e:
                raise SaveJsonError(f'Error when saving JSON => {e}')

            try:
                # upload_to_s3(local_path, s3_path.replace('s3://', ''))
                print(f'{filename_json} success upload to s3 == {s3_path}')
            except UploadS3Error as e:
                await e.send_message()
            except Exception as e:
                raise UploadS3Error(f'Error when upload to s3 => {e}')