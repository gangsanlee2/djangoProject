from django.urls import re_path as url
from movie.movies import views

urlpatterns = [
    url(r'movies', views.movies)
]