from django.urls import re_path as url

from basic.mlearn.stroke import views

urlpatterns = [
    url(r'stroke', views.stroke)
]