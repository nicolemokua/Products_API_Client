# Product_API_Client
(product_API_client). This document will guide anyone who wants to set up, use, and test the client script that interacts with the Product API.

---

# *Product API Client*

This repository contains a Python client for interacting with the *Product API*. The client allows you to perform two primary actions:
1. *Add a new product* to the Product API.
2. *Retrieve a list of all products* from the Product API.

---

## *Features*
- *Add a new product* using the POST method.
- *Retrieve all products* using the GET method.

---

## *Prerequisites*

Make sure you have the following installed on your system:

1. *Python 3.8+*: [Download Python](https://www.python.org/downloads/)
2. *pip*: Python's package installer (comes with Python).
3. *requests library*: This is used to send HTTP requests. You can install it by running:
   bash
   pip install requests
   
4. *Virtual Environment (optional but recommended)*: To manage dependencies separately for your project.

---

## *Setup Instructions*

### *1. Clone the Repository*

Clone this repository to your local machine:
bash
git clone https://github.com/nicolemokua/Products_API_Client.git
cd product-api-client


### *2. Create a Virtual Environment (Optional but Recommended)*

You can create a virtual environment to isolate the dependencies for this project:

#### On Windows:
bash
python -m venv .venv
.\.venv\Scripts\activate


#### On macOS/Linux:
bash
python3 -m venv .venv
source .venv/bin/activate


### *3. Install Dependencies*

Once the virtual environment is activated, install the required dependencies (requests library):

bash
pip install -r requirements.txt


If you don’t have a requirements.txt file, you can manually install requests:
bash
pip install requests


### *4. Configure the API Endpoint*

Ensure that the *Product API* server is running on your local machine. You can use the provided Django API (Product API) or any other API endpoint that matches the following:

- *Base URL* for the Product API: http://127.0.0.1:8000/api/products/
  
### *5. Start the Product API Server*

The client interacts with the API, so make sure the *Product API* server is running before using the client. In your *Product API* directory, run:
bash
python manage.py runserver


---

## *Using the Client Script*

### *1. Run the Client Script*

Once the server is up and running, you can test the client script by running:

bash
python client_script.py


### *2. Client Script Functions*

The client_script.py has two main functions:

#### **a) add_product()**
This function sends a POST request to the Product API to create a new product. The data for the new product is hardcoded in the script but can be modified as needed.

Example product data:

json
{
    "name": "Laptop",
    "description": "A high-performance laptop",
    "price": 1200.00
}


#### **b) get_products()**
This function sends a GET request to the API to retrieve a list of all products. The products will be printed in the console as JSON.

---

## *Testing the Client Script*

Once the client script is running, you should see output like this:

1. *For Adding a Product*:
   bash
   Running client script...
   Attempting to add product...
   Product created successfully: {"name": "Laptop", "description": "A high-performance laptop", "price": 1200.00}
   

2. *For Retrieving Products*:
   bash
   Attempting to retrieve products...
   Products: [{"name": "Laptop", "description": "A high-performance laptop", "price": 1200.00}]
   

---

## *Testing the API Manually with Postman or cURL*

If you want to manually test the API using Postman or cURL, here’s how:

### *1. Test POST Request (Create Product)*

- *URL*: http://127.0.0.1:8000/api/products/create/
- *Method*: POST
- *Body* (raw, JSON):
  json
  {
      "name": "Laptop",
      "description": "A high-performance laptop",
      "price": 1200.00
  }
  

### *2. Test GET Request (List Products)*

- *URL*: http://127.0.0.1:8000/api/products/
- *Method*: GET

You should receive a JSON response containing all the products in the database.

---

## *Directory Structure*

product-api-client/
├── client_script.py         # The Python client script
├── .venv/                   # Virtual environment directory (optional)
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation (this file)


---

## *Common Issues and Troubleshooting*

### *1. "Connection Refused" Error*

- Ensure that the *Product API* server is running and accessible.
- Check the URL in client_script.py to make sure it matches the Product API’s running server URL.

### *2. "404 Not Found" Error*

- Double-check that the endpoint URLs are correctly defined in the Product API and that the server is running.
- Verify that the URL in BASE_URL in client_script.py matches the correct API endpoint.

---

## *Contributing*

Feel free to submit pull requests if you want to add more features or improve the functionality of this client. You can also open an issue if you encounter any bugs or have questions.

---

## *License*

This project is licensed under the MIT License.

---

### *How to Push to GitHub*

Once your changes are ready and committed, follow these steps to push the client script to a GitHub repository:

1. *Initialize Git* (if not already initialized):
   bash
   git init
   

2. *Add all files* to Git:
   bash
   git add .
   

3. *Commit the changes*:
   bash
   git commit -m "Initial commit for product API client"
   

4. *Add your remote repository* https://github.com/nicolemokua/Products_API_Client.git:
   bash
   git remote add origin https://github.com/nicolemokua/Products_API_Client.git
   

5. *Push the changes*:
   bash
   git push -u origin main
   

---

### *Conclusion*

With this README.md, users will have detailed instructions for setting up the *Product API Client*, using it, and troubleshooting common issues. Feel free to customize it further based on your specific project needs!