from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# initial data
data = [
    {
        "id": 1,
        "name": "Book",
        "price": 9.99,
        "url": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "You can read it!"
    },
    {
        "id": 2,
        "name": "Headphones",
        "price": 249.99,
        "url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Listen to stuff!"
    },
    {
        "id": 3,
        "name": "Backpack",
        "price": 79.99,
        "url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Carry things around town!"
    },
    {
        "id": 4,
        "name": "Glasses",
        "price": 129.99,
        "url": "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Now you can see!"
    },
    {
        "id": 5,
        "name": "Cup",
        "price": 4.99,
        "url": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Drink anything with it!"
    },
    {
        "id": 6,
        "name": "Shirt",
        "price": 29.99,
        "url": "https://images.unsplash.com/photo-1581655353564-df123a1eb820?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=800&q=80",
        "description": "Wear it with style!"
    }
]


def get_item_by_id(item_id):
    return next((item for item in data if item['id'] == item_id), None)


@method_decorator(csrf_exempt, name='dispatch')
class ItemListView(View):
    def get(self, request):
        return JsonResponse(data, safe=False, status=200)

    def post(self, request):
        new_item = json.loads(request.body)

        if not all(key in new_item for key in ["name", "price", "url", "description"]):
            return JsonResponse({'error': 'Invalid item format'}, status=400)

        data.append(new_item)
        return JsonResponse(new_item, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ItemDetailView(View):
    def get(self, request, item_id):
        item = get_item_by_id(item_id)
        if item is None:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(item, status=200)

    def put(self, request, item_id):
        item = get_item_by_id(item_id)
        if item is None:
            return JsonResponse({'error': 'Not found'}, status=404)
        item.update(json.loads(request.body))
        return JsonResponse(item, status=200)

    def delete(self, request, item_id):
        global data
        data = [item for item in data if item['id'] != item_id]
        return JsonResponse({'result': 'Success'}, status=200)
