from django.urls import re_path as url  # re_path는 path 뒤에 추가로 붙는 경로를 뜻한다.

from basic.nlp import views

urlpatterns = [
    url(r'samsung-report', views.samsung_report),  # GET
    url(r'naver-movie-review', views.naver_movie_review),  # GET
]