from rest_framework import serializers

from movie.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    director = serializers.CharField()
    description = serializers.CharField()
    poster_url = serializers.CharField()
    running_time = serializers.IntegerField()
    age_rating = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Movie.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
