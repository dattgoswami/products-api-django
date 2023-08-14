# Product API Django

This Django project serves a list of products that are stored in memory. You can list, view, add, modify, or delete products via this API.

## Prerequisites

- Python
- Django

### Install Dependencies:

pip install django

## Running the Project

1. Navigate to the project directory
2. Run the Django development server:

```
python manage.py runserver
```

Now, you can access the API at `http://localhost:8000/items/`.

## Endpoints

1. List all items:

   - URL: `/items/`
   - Method: `GET`

2. Add a new item:

   - URL: `/items/`
   - Method: `POST`
   - Body: JSON of the item (with fields "id, "name", "price", "url", "description")

3. View an item by ID:

   - URL: `/items/<item_id>/`
   - Method: `GET`

4. Update an item by ID:

   - URL: `/items/<item_id>/`
   - Method: `PUT`
   - Body: JSON of the fields to update

5. Delete an item by ID:
   - URL: `/items/<item_id>/`
   - Method: `DELETE`

**Note:** CSRF protection is disabled for simplicity in this example. Make sure to implement and handle CSRF protection properly in production deployments.
