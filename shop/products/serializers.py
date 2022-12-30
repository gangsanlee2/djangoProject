from rest_framework import serializers
from shop.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.CharField()
    image_url = serializers.CharField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Product.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
