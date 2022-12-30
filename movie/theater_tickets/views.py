from rest_framework.decorators import api_view

from movie.movies.repositories import MovieRepository
from movie.movies.serializers import MovieSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def theater_ticket(request):
    if request.method == 'POST':
        return MovieSerializer().create(request.data)
    elif request.method == 'PUT':
        return MovieSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return MovieSerializer().delete(request.data)
    elif request.method == 'GET':
        return MovieRepository().find_by_id(request.data)

@api_view(['GET'])
def theater_ticket_list(request): return MovieRepository().get_all(request.data)

