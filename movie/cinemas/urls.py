from django.urls import re_path as url
from movie.cinemas import views

urlpatterns = [
    url(r'cinemas', views.cinemas)
]