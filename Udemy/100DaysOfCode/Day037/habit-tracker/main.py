import os
import requests
from datetime import datetime

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": "20230606",
    "quantity": "15"
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_endpoint_put = f"{graph_endpoint}/{GRAPH_ID}/20230606"
pixel_data_put = {
    "quantity": "4"
}

# response = requests.put(url=pixel_endpoint_put, json=pixel_data_put, headers=headers)
# print(response.text)

pixel_endpoint_delete = pixel_endpoint_put
response = requests.delete(url=pixel_endpoint_delete, headers=headers)
print(response.text)

today = datetime.today()
