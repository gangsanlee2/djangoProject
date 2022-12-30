from rest_framework.response import Response

from shop.products.models import Product
from shop.products.serializers import ProductSerializer


class ProductRepository(object):
    def __init__(self):
        print("ProductRepository 객체 생성")

    def get_all(self):
        return Response(ProductSerializer(Product.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(ProductSerializer(Product.objects.all(), many=True).data)