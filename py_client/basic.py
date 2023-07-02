import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"content": "guy ronen"})
print(response.json())
