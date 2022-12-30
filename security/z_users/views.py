from rest_framework.decorators import api_view
from security.z_users.repositories import UserRepository
from security.z_users.serializers import UserSerializer

@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def user(request):
    if request.method == 'POST':
        return UserSerializer().create(request.data)
    elif request.method == 'PUT':
        return UserSerializer().update(request.data)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        return UserSerializer().delete(request.data)
    elif request.method == 'GET':
        return UserRepository().find_by_id(request.data)

@api_view(['GET'])
def user_list(request): return UserRepository().get_all()

@api_view(['Post'])
def login(request): return UserRepository().login(request.data)
