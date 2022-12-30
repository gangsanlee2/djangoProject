from rest_framework.response import Response

from shop.deliveries.models import Delivery
from shop.deliveries.serializers import DeliverySerializer


class DeliveryRepository(object):
    def __init__(self):
        print("DeliveryRepository 객체 생성")

    def get_all(self):
        return Response(DeliverySerializer(Delivery.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(DeliverySerializer(Delivery.objects.all(), many=True).data)