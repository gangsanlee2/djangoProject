from rest_framework.decorators import api_view

from blog.tags.repositories import TagRepository
from blog.tags.serializers import TagSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def tag(request):
    if request.method == 'POST':
        return TagSerializer().create(request.data)
    elif request.method == 'PUT':
        return TagSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return TagSerializer().delete(request.data)
    elif request.method == 'GET':
        return TagRepository().find_by_id(request.data)

@api_view(['GET'])
def tag_list(request): return TagRepository().get_all(request.data)
