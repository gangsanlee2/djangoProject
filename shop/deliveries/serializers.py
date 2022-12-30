from rest_framework import serializers

from shop.deliveries.models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    parent_id = serializers.CharField()

    class Meta:
        model = Delivery
        fields = '__all__'

    def create(self, validated_data):
        return Delivery.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Delivery.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
