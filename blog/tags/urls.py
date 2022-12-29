from django.urls import re_path as url
from blog.tags import views

urlpatterns = [
    url(r'tags', views.tags)
]