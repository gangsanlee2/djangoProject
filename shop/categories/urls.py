from django.urls import re_path as url
from shop.categories import views

urlpatterns = [
    url(r'categories', views.categories)
]