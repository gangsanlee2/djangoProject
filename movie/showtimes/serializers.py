from rest_framework import serializers

from movie.showtimes.models import Showtime


class ShowtimeSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    class Meta:
        model = Showtime
        fields = '__all__'

    def create(self, validated_data):
        return Showtime.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Showtime.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
