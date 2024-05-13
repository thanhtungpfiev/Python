# Created by Admin at 5/23/2022
import os
from secrets import token_hex
import requests

PICS_FOLDER = 'pics'
URL = 'https://unsplash.com/photos'


def download(url):
    resp = requests.get(url)
    return save_image(resp.content)


def save_image(content):
    filename = '{}.jpeg'.format(token_hex(4))
    path = os.path.join(PICS_FOLDER, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as stream:
        stream.write(content)
    return filename


def batch_download(url, n):
    return [download(url) for _ in range(n)]


if __name__ == '__main__':
    saved = batch_download(URL, 10)
    print(saved)
