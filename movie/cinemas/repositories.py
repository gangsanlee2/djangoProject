from rest_framework.response import Response

from movie.cinemas.models import Cinema
from movie.cinemas.serializers import CinemaSerializer


class CinemaRepository(object):
    def __init__(self):
        print("CinemaRepository 객체 생성")

    def get_all(self):
        return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)