import s3fs
import logging
from src.exception.exception import UploadS3Error

logger = logging.getLogger(__name__)
def upload_to_s3(local_path, s3_path):
    client_kwargs = {
        'key': 'GLZG2JTWDFFSCQVE7TSQ',
        'secret': 'VjTXOpbhGvYjDJDAt2PNgbxPKjYA4p4B7Btmm4Tw',
        'endpoint_url': 'http://10.12.1.149:8000',
        'anon': False
    }

    s3 = s3fs.S3FileSystem(**client_kwargs)
    try:
        s3.put(local_path, s3_path)
        if s3.exists(s3_path):
            logger.info('File upload successfully')
        else:
            logger.info('File upload failed')
    except Exception as e:
        logger.error(f'Upload failed: {e}')
        raise UploadS3Error(f'Error when upload to s3 => {e}')
