import requests

endpoint = "http://localhost:8000/api/products/"

# POST

post_data = {
    "title": "New Product using json",
    "price": 1000.00,
}

post_response = requests.post(endpoint, json=post_data)
print(post_response.json())