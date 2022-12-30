from rest_framework import serializers

from movie.cinemas.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    image_url = serializers.CharField()
    address = serializers.CharField()
    detail_address = serializers.CharField()


    class Meta:
        model = Cinema
        fields = '__all__'

    def create(self, validated_data):
        return Cinema.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Cinema.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
