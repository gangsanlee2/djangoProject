from django.urls import re_path as url
from blog.views import views

urlpatterns = [
    url(r'views', views.views)
]