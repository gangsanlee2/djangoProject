from rest_framework.decorators import api_view

from shop.carts.repositories import CartRepository
from shop.carts.serializers import CartSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def cart(request):
    if request.method == 'POST':
        return CartSerializer().create(request.data)
    elif request.method == 'PUT':
        return CartSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return CartSerializer().delete(request.data)
    elif request.method == 'GET':
        return CartRepository().find_by_id(request.data)

@api_view(['GET'])
def cart_list(request): return CartRepository().get_all(request.data)
