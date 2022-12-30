from rest_framework.decorators import api_view

from shop.products.repositories import ProductRepository
from shop.products.serializers import ProductSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def product(request):
    if request.method == 'POST':
        return ProductSerializer().create(request.data)
    elif request.method == 'PUT':
        return ProductSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return ProductSerializer().delete(request.data)
    elif request.method == 'GET':
        return ProductRepository().find_by_id(request.data)

@api_view(['GET'])
def product_list(request): return ProductRepository().get_all(request.data)
