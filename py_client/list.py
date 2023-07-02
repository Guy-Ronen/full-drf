import requests

endpoint = "http://localhost:8000/api/products/"

# GET
get_response = requests.get(endpoint)
print(get_response.json())
