import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from dlearn.fashion_service import FashionService
'''
@api_view(["GET"])
def getFashion(request, testNum):
    print(f"######## GET at Here ! React testNum is {request.GET['testNum']} ########")
    return JsonResponse({'result': FashionService().service_model(int(request.GET['testNum']))})

@api_view(["POST"])
def postFashion(request):
    data = json.loads(request.body)  # json to dict
    print(f"######## POST at Here ! React testNum is {data['testNum']} ########")
    return JsonResponse({'result': FashionService().service_model(int(data['testNum']))})
'''
@api_view(['GET', 'POST'])
def fashion(request):
    if request.method == 'GET':
        print(f"######## ID is {request.GET['id']} ########")
        return JsonResponse(
            {'result': FashionService().service_model(int(request.GET['id']))})
    elif request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## ID is {data['id']} ########")
        return JsonResponse({'result': FashionService().service_model(int(data['id']))})
'''
@api_view(['GET'])
@parser_classes([JSONParser])
def fashion(request):
    if request.method == 'GET':
        body = request.body
        data = json.loads(body)

        print(request.headers)
        print(request.content_type)
        print(f'##### React ID is {data} ##### ')
        resp = "TEST SUCCESS !!"
        return JsonResponse({'result':resp})
    else:
        print(f"##### React ID is None ##### ")
'''
'''
@api_view(['POST'])
@parser_classes([JSONParser])
def fashion(request):
    data = request.data

    test_num = tf.constant(int(data['testNum']))

    print(f'리액트에서 보낸 데이터 : {data}')
    print(f'test_num type : {type(test_num)}')

    result = FashionService().service_model(test_num)
    if result == 0:
        resp = 'T-shirt/top'
    elif result == 1:
        resp = 'Trouser'
    elif result == 2:
        resp = 'Pullover'
    elif result == 3:
        resp = 'Dress'
    elif result == 4:
        resp = 'Coat'
    elif result == 5:
        resp = 'Sandal'
    elif result == 6:
        resp = 'Shirt'
    elif result == 7:
        resp = 'Sneaker'
    elif result == 8:
        resp = 'Bag'
    elif result == 9:
        resp = 'Ankle boot'
    return JsonResponse({'result': resp})
'''