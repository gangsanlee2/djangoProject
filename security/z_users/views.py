from django.http import JsonResponse
from rest_framework.authtoken.models import Token
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

@api_view(['Post'])
@parser_classes([JSONParser])
def login(request):
    try:
        print(f"로그인 정보: {request.data}")
        loginInfo = request.data
        loginUser = User.objects.get(user_email=loginInfo['user_email'])
        print(f'해당 email 을 가진 User:\n {loginUser}')
        if loginUser.password == loginInfo['password']:
            dbUser = User.objects.all().filter(id=loginUser.id).values()[0]
            print(f" DBUser is {dbUser}")
            serializer = UserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
            # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return Response("WRONG PASSWORD")
    except:
        return Response("WRONG EMAIL")