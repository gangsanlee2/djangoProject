import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from nlp.samsung_report.services import Controller




@api_view(['GET'])
def samsung_report(request):
    return JsonResponse({'result': Controller().hook()})
