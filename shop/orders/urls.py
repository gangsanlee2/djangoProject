from django.urls import re_path as url
from shop.orders import views

urlpatterns = [
    url(r'orders', views.orders)
]