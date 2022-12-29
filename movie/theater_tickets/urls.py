from django.urls import re_path as url
from movie.theater_tickets import views

urlpatterns = [
    url(r'theater-tickets', views.theater_tickets)
]