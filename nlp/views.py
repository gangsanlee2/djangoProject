from django.http import JsonResponse
from rest_framework.decorators import api_view

from nlp.samsung_report.services import Controller


@api_view(['GET'])
def samsung_report(request):
    return JsonResponse({'result': Controller().hook()})
