from django.urls import re_path as url
from shop.orders import views

urlpatterns = [
    url(r'order$', views.order),
    url(r'order-list', views.order_list),
]