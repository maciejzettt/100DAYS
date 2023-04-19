import requests
import pixela_auth
import datetime

today = datetime.date.strftime(datetime.date.today(), "%Y%m%d")

endpoint = f"https://pixe.la/v1/users/{pixela_auth.USERNAME}/graphs/{pixela_auth.GRAPH_ID}/20230419"

params = {
    "quantity": "51"
}

headers = {
    "X-USER-TOKEN": pixela_auth.TOKEN
}

response = requests.put(url=endpoint, json=params, headers=headers)

print(response.text)