from rest_framework.decorators import api_view
from blog.b_users.repositories import BUserRepository
from blog.b_users.serializers import BUserSerializer

@api_view(['GET', 'Post', 'PUT', 'PATCH', 'DELETE'])
def b_user(request):
    if request.method == 'POST':
        return BUserSerializer().create(request.data)
    elif request.method == 'PUT':
        return BUserSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return BUserSerializer().delete(request.data)
    elif request.method == 'GET':
        return BUserRepository().find_by_id(request.data)

@api_view(['GET'])
def b_user_list(request): return BUserRepository().get_all(request.data)

@api_view(['Post'])
def login_buser(request): return BUserRepository().login(request.data)
