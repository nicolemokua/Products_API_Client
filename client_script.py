import requests

BASE_URL = "http://127.0.0.1:8000/api/products/"

# Add a new product
def add_product():
    print("Attempting to add product...")  # Debugging print statement
    product = {
        "name": "Iphone 13",
        "description": "Good performance with ios 18",
        "price": 80000.00
    }
    response = requests.post(BASE_URL + "create/", json=product)
    if response.status_code == 201:
        print("Product created successfully:", response.json())
    else:
        print("Failed to create product:", response.json())

# Retrieve all products
def get_products():
    print("Attempting to retrieve products...")  # Debugging print statement
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to retrieve products:", response.status_code)

if __name__ == "__main__":
    print("Running client script...")
    add_product()
    get_products()