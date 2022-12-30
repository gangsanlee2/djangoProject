from rest_framework.decorators import api_view

from shop.orders.repositories import OrderRepository
from shop.orders.serializers import OrderSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def order(request):
    if request.method == 'POST':
        return OrderSerializer().create(request.data)
    elif request.method == 'PUT':
        return OrderSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return OrderSerializer().delete(request.data)
    elif request.method == 'GET':
        return OrderRepository().find_by_id(request.data)

@api_view(['GET'])
def order_list(request): return OrderRepository().get_all(request.data)
