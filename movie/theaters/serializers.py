from rest_framework import serializers

from movie.theaters.models import Theater


class TheaterSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    seat = serializers.CharField()

    class Meta:
        model = Theater
        fields = '__all__'

    def create(self, validated_data):
        return Theater.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Theater.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
