from rest_framework.decorators import api_view

from shop.deliveries.repositories import DeliveryRepository
from shop.deliveries.serializers import DeliverySerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def delivery(request):
    if request.method == 'POST':
        return DeliverySerializer().create(request.data)
    elif request.method == 'PUT':
        return DeliverySerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return DeliverySerializer().delete(request.data)
    elif request.method == 'GET':
        return DeliveryRepository().find_by_id(request.data)

@api_view(['GET'])
def delivery_list(request): return DeliveryRepository().get_all(request.data)
