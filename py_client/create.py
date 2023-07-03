import requests

endpoint = "http://localhost:8000/api/products/"

# POST

post_data = {
    "title": "New Product using json",
    "price": 1000.00,
}

response = requests.post(endpoint, json=post_data)
print(response.json())
