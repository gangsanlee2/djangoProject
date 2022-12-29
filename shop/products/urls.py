
from django.urls import re_path as url
from shop.products import views

urlpatterns = [
    url(r'products', views.products)
]