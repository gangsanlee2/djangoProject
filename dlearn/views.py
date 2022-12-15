from django.http import JsonResponse
from matplotlib import pyplot as plt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from dlearn.fashion_service import FashionService


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
