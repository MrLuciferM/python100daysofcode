import requests
from datetime import date

pixela_endpoint = "https://pixe.la/v1/users"  #{"token":"thisissecret", "username":"a-know", "":"yes", "notMinor":"yes"}

USER_TOKEN = "BBFDB5DG54E7454512AS1A15RG4RA"
USERNAME = "kunal"
GRAPH_ID = "graph1"

# user_parameters = {
#     "token": USER_TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# Creating new user account

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# response.raise_for_status()
# print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "learning",
#     "unit": "Hrs",
#     "type": "float",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": USER_TOKEN
}


# Creating a new graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# print(response.json())

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = date.today()
today_date = today.strftime("%Y%m%d")

pixel_data = {
    "date": today_date,
    "quantity": input("How many hours did you study today?(decimal value): ")
}

# Adding the pixel data

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
response.raise_for_status()
print(response.json())

# pixel_update_endpoint = f"{pixel_endpoint}/{today_date}"

# pixel_update_data = {
#     "quantity" : "1.2"
# }

# Updating a pixel

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# response.raise_for_status()
# print(response.json())

# Deleting a pixel

# pixel_delete_endpoint = f"{pixel_endpoint}/20210624"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# response.raise_for_status()

# print(response.json())