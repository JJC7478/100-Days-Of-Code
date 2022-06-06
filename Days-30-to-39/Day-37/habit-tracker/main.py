from time import strftime
import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(user_response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

g1_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5"
}


# response = requests.post(url=g1_endpoint, json=pixel_data, headers=headers)
# print(response.text)

g1_update_endpoint = f"{g1_endpoint}/20220605"

pixel_update = {
    "quantity": "1.2"
}

# response = requests.put(url=g1_update_endpoint,json=pixel_update, headers=headers)
# print(response.text)

# response = requests.delete(url=g1_update_endpoint, headers=headers)
# print(response.text)