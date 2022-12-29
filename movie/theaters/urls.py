from django.urls import re_path as url
from movie.theaters import views

urlpatterns = [
    url(r'theaters', views.theaters)
]