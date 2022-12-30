from django.urls import re_path as url
from blog.tags import views

urlpatterns = [
    url(r'tag$', views.tag),
    url(r'tag_list', views.tag_list)
]