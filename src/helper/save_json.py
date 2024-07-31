import json
import os
from datetime import datetime
from typing import Any, Dict

class SaveJson:
    response: Any  
    kategori: str
    s3_path: str
    data: Dict[str, Any]
    tahun: int
    tag : str

    def __init__(self, response: Any, s3_path: str,  data: Dict[str, Any], tahun: int, tag: str):  
        self.response = response
        self.s3_path = s3_path
        self.data = data
        self.tahun = tahun
        self.tag = tag

    async def save_json_local(self, kategori, filename, tahun):
        if kategori == 'GPI':
            kategori = 'Global Peace Index'
        elif kategori == 'GTI':
            kategori = 'Global Terrorism Index'
        elif kategori == 'ETR':
            kategori = 'Ecological Threat Report'
        elif kategori == 'MPI':
            kategori = 'Mexico Peace Index'
        elif kategori == 'PPI':
            kategori = 'Positive Peace Index'
        elif kategori == 'USPI':
            kategori = 'US Peace Index'
        elif kategori == 'UKPI' or kategori == 'ukpi':
            kategori = 'UK Peace Index'

        directory = os.path.join('data', kategori.replace(' ', '_').lower(), tahun, 'json')
        os.makedirs(directory, exist_ok=True)
        filename_json = filename.replace(' ', '_').lower()
        file_path = os.path.join(directory, filename_json)

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.mapping(), json_file, ensure_ascii=False)


    def mapping(self):

        if self.tag == 'GPI':
            self.tag = 'Global Peace Index'
        elif self.tag == 'GTI':
            self.tag = 'Global Terrorism Index'
        elif self.tag == 'ETR':
            self.tag = 'Ecological Threat Report'
        elif self.tag == 'MPI':
            self.tag = 'Mexico Peace Index'
        elif self.tag == 'PPI':
            self.tag = 'Positive Peace Index'
        elif self.tag == 'USPI':
            self.tag = 'US Peace Index'
        elif self.tag == 'UKPI' or self.tag == 'ukpi':
            self.tag = 'UK Peace Index'
        

        full_data = {
            'link': self.response,
            'domain': self.response.split('/')[2],
            'tag': [
                self.response.split('/')[2],
                self.tahun,
                self.tag
            ],
            'crawling_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'crawling_time_epoch': int(datetime.now().timestamp()),
            'path_data_raw': self.s3_path,
            'path_data_clean': None,
            'tahun': self.tahun,
            'data': self.data
        }
        return full_data