from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.flower.iris_service import IrisService


@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    iris_info = request.data
    SepalLengthCm = iris_info['SepalLengthCm']
    SepalWidthCm = iris_info['SepalWidthCm']
    PetalLengthCm = iris_info['PetalLengthCm']
    PetalWidthCm = iris_info['PetalWidthCm']
    print(f'리액트에서 보낸 데이터 : {iris_info}cm')
    print(f'꽃받침 길이 : {SepalLengthCm}cm')
    print(f'꽃받침 너비 : {SepalWidthCm}cm')
    print(f'꽃잎 너비 : {PetalLengthCm}cm')
    print(f'꽃잎 너비 : {PetalWidthCm}cm')
    return JsonResponse({'데이터 전송 결과': '성공!!'})