from pprint import pprint

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
        
    def get_upload_link(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-type':'application/json',
            'Authorization':'OAuth {}'.format(self.token)
            }
        params = {"path": file_path, "overwrite":"true"}
        response = requests.get(url, headers = headers, params = params)
        data = response.json()
        href = data.get('href')
        return href
    
    def upload(self, file_path: str, name):
        href = self.get_upload_link(file_path=file_path)
        response = requests.put(href, data=open(name, 'rb'))
        if response.status_code == 201:
            print ('Успех')
        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ('pathon/test.txt')
    token = 'y0_AgAAAAAxjz1IAADLWwAAAADejWLqKC58MlQxQj6rrFnimCW8jOVasZs'
    uploader = YaUploader(token)
    name = 'test.txt'
    result = uploader.upload(path_to_file, name) 