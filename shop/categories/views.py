from rest_framework.decorators import api_view

from shop.categories.repositories import CategoryRepository
from shop.categories.serializers import CategorySerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def category(request):
    if request.method == 'POST':
        return CategorySerializer().create(request.data)
    elif request.method == 'PUT':
        return CategorySerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return CategorySerializer().delete(request.data)
    elif request.method == 'GET':
        return CategoryRepository().find_by_id(request.data)

@api_view(['GET'])
def category_list(request): return CategoryRepository().get_all(request.data)
