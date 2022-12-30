from rest_framework.decorators import api_view

from blog.views.repositories import ViewRepository
from blog.views.serializers import ViewSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def view(request):
    if request.method == 'POST':
        return ViewSerializer().create(request.data)
    elif request.method == 'PUT':
        return ViewSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return ViewSerializer().delete(request.data)
    elif request.method == 'GET':
        return ViewRepository().find_by_id(request.data)

@api_view(['GET'])
def view_list(request): return ViewRepository().get_all(request.data)
