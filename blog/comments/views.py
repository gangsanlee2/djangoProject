from rest_framework.decorators import api_view
from blog.comments.repositories import CommentRepository
from blog.comments.serializers import CommentSerializer


@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def comment(request):
    if request.method == 'POST':
        return CommentSerializer().create(request.data)
    elif request.method == 'PUT':
        return CommentSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return CommentSerializer().delete(request.data)
    elif request.method == 'GET':
        return CommentRepository().find_by_id(request.data)

@api_view(['GET'])
def comment_list(request): return CommentRepository().get_all(request.data)

