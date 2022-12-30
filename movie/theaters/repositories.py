from rest_framework.response import Response

from movie.theaters.models import Theater
from movie.theaters.serializers import TheaterSerializer


class TheaterRepository(object):
    def __init__(self):
        print("TheaterRepository 객체 생성")

    def get_all(self):
        return Response(TheaterSerializer(Theater.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(TheaterSerializer(Theater.objects.all(), many=True).data)