from django.urls import re_path as url
from shop.deliveries import views

urlpatterns = [
    url(r'delivery$', views.delivery),
    url(r'delivery-list', views.delivery_list),
]