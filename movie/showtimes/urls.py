from django.urls import re_path as url
from movie.showtimes import views

urlpatterns = [
    url(r'showtime$', views.showtime),
    url(r'showtime_list', views.showtime_list)
]