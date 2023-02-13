import requests


class YaUploader:

    def __init__(self, token_ya):
        self.token_ya = token_ya

    def _create_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_ya)
        }

    def get_create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self._create_header()
        params = {'path': 'Test', "overwrite": "true"}
        response = requests.put(url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    with open('token.txt', 'r') as file_object:
        token_ya = file_object.read().strip()
        yandex = YaUploader(token_ya)
        yandex.get_create_folder()
        print(yandex.get_create_folder())
