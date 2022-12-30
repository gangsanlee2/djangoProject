from rest_framework.decorators import api_view

from movie.cinemas.repositories import CinemaRepository
from movie.cinemas.serializers import CinemaSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def cinema(request):
    if request.method == 'POST':
        return CinemaSerializer().create(request.data)
    elif request.method == 'PUT':
        return CinemaSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return CinemaSerializer().delete(request.data)
    elif request.method == 'GET':
        return CinemaRepository().find_by_id(request.data)
@api_view(['GET'])
def cinema_list(request): return CinemaRepository().get_all(request.data)
