from rest_framework.response import Response

from movie.movies.models import Movie
from movie.movies.serializers import MovieSerializer


class MovieRepository(object):
    def __init__(self):
        print("MovieRepository 객체 생성")

    def get_all(self):
        return Response(MovieSerializer(Movie.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(MovieSerializer(Movie.objects.all(), many=True).data)