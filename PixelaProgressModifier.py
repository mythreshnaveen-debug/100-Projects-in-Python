import requests
from datetime import datetime

# Project 37 - Pixela Progress Modifier!
# This modifies your pixela progress, without having that pesky rejection thing, that you get if you are not a donator.
# This also automatically gets today's date, and sends it over.


pixela_endpoint = "https://pixe.la/v1/users"


USER_TOKEN =  input("What is your Pixela Token?")
USERNAME = input("What is your Pixela username?")


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/"

graph_config = {
    "id": input("What is the id of the graph you want to modify?"),
    "name": input("What is the name of the graph you want to modify?"),
}

edit_graph_endpoint = graph_endpoint + graph_config["id"]
now = datetime.now()


body = {
    "date": str(now.year) + str(now.month) + str(now.day),
    "quantity": input("What is the quantity of the new listing?")
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}


response = requests.post(url=edit_graph_endpoint, json=body, headers=headers)
while str(response) == "<Response [503]>":
    response = requests.post(url=edit_graph_endpoint, json=body, headers=headers)
print(f"Updated! Go check out {edit_graph_endpoint}!")
