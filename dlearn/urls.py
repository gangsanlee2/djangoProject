from django.urls import re_path as url

from dlearn import views

urlpatterns = [
    url(r'fashion', views.fashion)
]