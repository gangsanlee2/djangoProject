from django.http import JsonResponse
from rest_framework.decorators import api_view

from webcrawler.services import ScrapService


@api_view(['GET'])
def crawler(request):
        return JsonResponse(
            {'result': ScrapService().naver_movie_review()})
