from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.b_users.services import UserService


@api_view(['Post'])
@parser_classes([JSONParser])
def login(request):
    user_info = request.data
    email = user_info['email']
    password = user_info['password']
    print(f'리액트에서 보낸 데이터 : {user_info}')
    print(f'넘어온 이메일 : {email}')
    print(f'넘어온 비밀번호 : {password}')
    return JsonResponse({'로그인 결과': '성공!!'})

@api_view(['GET'])
@parser_classes([JSONParser])
def signup(request):
    #UserService().create_users()
    return JsonResponse({'회원가입 결과': '성공!!'})