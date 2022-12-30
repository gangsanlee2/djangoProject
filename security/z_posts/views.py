from rest_framework.decorators import api_view

from security.z_posts.repositories import PostRepository
from security.z_posts.serializers import PostSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def post(request):
    if request.method == 'POST':
        return PostSerializer().create(request.data)
    elif request.method == 'PUT':
        return PostSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return PostSerializer().delete(request.data)
    elif request.method == 'GET':
        return PostRepository().find_by_id(request.data)

@api_view(['GET'])
def post_list(request): return PostRepository().get_all(request.data)

