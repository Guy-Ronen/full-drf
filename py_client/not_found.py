import requests

endpoint = "http://localhost:8000/api/products/1053248975092345/"
# GET
get_response = requests.get(endpoint)
print(get_response.json())
