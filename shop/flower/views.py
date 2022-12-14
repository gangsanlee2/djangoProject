from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.flower.iris_service import IrisService
import tensorflow as tf

@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    iris_info = request.data
    SepalLengthCm = tf.constant(float(iris_info['SepalLengthCm']))
    SepalWidthCm = tf.constant(float(iris_info['SepalWidthCm']))
    PetalLengthCm = tf.constant(float(iris_info['PetalLengthCm']))
    PetalWidthCm = tf.constant(float(iris_info['PetalWidthCm']))
    print(f'리액트에서 보낸 데이터 : {iris_info}cm')
    print(f'꽃받침 길이 : {SepalLengthCm}cm')
    print(f'꽃받침 너비 : {SepalWidthCm}cm')
    print(f'꽃잎 너비 : {PetalLengthCm}cm')
    print(f'꽃잎 너비 : {PetalWidthCm}cm')
    result = IrisService().service_model([SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm])
    if result == 0:
        print('찾는 품종: setosa / 부채붓꽃')
    elif result == 1:
        print('찾는 품종: versicolor / 버시칼라 ')
    elif result == 2:
        print('찾는 품종: virginica / 버지니카')
    return JsonResponse({'result':{result}})