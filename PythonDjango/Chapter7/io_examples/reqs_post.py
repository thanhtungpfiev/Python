# Created by Admin at 5/19/2022
import requests

url = 'https://httpbin.org/post'
data = {'title': 'Learn Python Programming'}

resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())
