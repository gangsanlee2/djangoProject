import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from basic.nlp.imdb.services import NaverMovieService
from basic.nlp.samsung_report.services import Controller


@api_view(['GET'])
def samsung_report(request):
    return JsonResponse({'result': Controller().hook()})

@api_view(['POST'])
def naver_movie_review(request):
    data = json.loads(request.body)
    result = '{:.2%}'.format(NaverMovieService().process(data))
    return JsonResponse({'result': result})