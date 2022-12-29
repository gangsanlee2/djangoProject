from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.z_users.models import User
from security.z_users.serializers import UserSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request):
    if request.method == "GET":
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

if __name__ == '__main__':
    print(UserSerializer(User.objects.all(), many=True).data['password'])