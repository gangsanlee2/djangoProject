
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import datetime

@api_view(['GET'])
@parser_classes([JSONParser])
def orders(request):
    print(f'*** Orders View At {datetime.datetime.now()} ***  {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})