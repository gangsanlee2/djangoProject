from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.flower.iris import Iris


@api_view(['GET'])
@parser_classes([JSONParser])
def iris(request):
    Iris().hook()
    print(f'Enter Stroke with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})