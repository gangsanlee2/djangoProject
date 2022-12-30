from django.urls import re_path as url
from movie.movies import views

urlpatterns = [
    url(r'movie$', views.movie),
    url(r'movie_list', views.movie_list)
]