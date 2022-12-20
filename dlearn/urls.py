from django.urls import re_path as url  # re_path는 path 뒤에 추가로 붙는 경로를 뜻한다.

from dlearn import views, number_view

urlpatterns = [
    url(r'fashion/(?P<id>)$', views.fashion),  # GET
    url(r'fashion', views.fashion), # POST
    url(r'number/(?P<id>)$', number_view.number),  # GET
    url(r'number', number_view.number), # POST
]