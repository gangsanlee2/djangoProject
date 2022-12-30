from django.urls import re_path as url
from movie.theaters import views

urlpatterns = [
    url(r'theater$', views.theater),
    url(r'theater-list', views.theater_list)
]