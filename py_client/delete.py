import requests

product_id = input("Enter product id you want to delete: ")

try:
    product_id = int(product_id)
except:
    print("Invalid id")
    product_id = None

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    response = requests.delete(endpoint)
    if response.status_code == 204:
        print(f"Product {product_id} deleted successfully")
    else:
        print(response.status_code, "Something went wrong")
