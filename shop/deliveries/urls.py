from django.urls import re_path as url
from shop.deliveries import views

urlpatterns = [
    url(r'deliveries', views.deliveries)
]