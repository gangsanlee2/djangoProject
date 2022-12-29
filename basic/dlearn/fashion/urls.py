from django.urls import re_path as url  # re_path는 path 뒤에 추가로 붙는 경로를 뜻한다.

from basic.dlearn.fashion import views

urlpatterns = [
    url(r'fashion/(?P<id>)$', views.fashion),  # GET
    url(r'fashion', views.fashion), # POST
]