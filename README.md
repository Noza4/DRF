# DRF

# Market Django REST Framework Project

This Django project, named Market, is designed to manage products using RESTful APIs. Below are the endpoints available for creating, updating, deleting, and retrieving information about products from the database.

## Endpoints

### Create Product
- URL: `/product/create`
- Method: POST
- Description: Use this endpoint to create a new product by providing the necessary information in the request body.

### Delete Product
- URL: `/product/delete/<id>`
- Method: DELETE
- Description: Delete a specific product from the database by providing its unique identifier (`id`) in the URL.

### Product Information
- URL: `/product/info`
- Method: GET
- Description: Retrieve information about all products stored in the database.

### Update Product
- URL: `/product/update/<id>`
- Method: PUT
- Description: Update the stock number of a specific product in the database by providing its unique identifier (`id`) in the URL and the new stock number in the request body.

### Product Listing
- URL: `/product/listing`
- Method: GET
- Description: Retrieve a listing of all products including their names and prices.

## Getting Started

To set up this project locally, follow these steps:

1. Clone this repository: git clone <repository-url>
2. Navigate to the project directory:cd market_project
3. Install dependencies: pip install -r requirements.txt
4. Apply migrations to create necessary database tables: python manage.py migrate
5. Run the development server: python manage.py runserver
