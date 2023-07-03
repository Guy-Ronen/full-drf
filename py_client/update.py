import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {"title": "Updated title", "price": 888.88}

request = requests.put(endpoint, data=data)
print(request.json())
