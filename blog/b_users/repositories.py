from django.http import JsonResponse
from rest_framework.response import Response

from blog.b_users.models import BUser
from blog.b_users.serializers import BUserSerializer


class BUserRepository(object):
    def __init__(self):
        print("BUserRepository 객체 생성")

    def login(self, login_info):
        loginUser = BUser.objects.get(user_email=login_info['user_email'])
        print(f"해당 email 을 가진  User ID: *** \n {loginUser.id}")
        if loginUser.password == login_info['password']:
            dbUser = BUser.objects.all().filter(id=loginUser.id).values()[0]
            print(f" DBUser is {dbUser}")
            serializer = BUserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return JsonResponse({"data": "WRONG_PASSWORD"})

    def get_all(self):
        return Response(BUserSerializer(BUser.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(BUserSerializer(BUser.objects.all(), many=True).data)