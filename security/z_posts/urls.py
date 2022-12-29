
from django.urls import re_path as url
from security.z_posts import views

urlpatterns = [
    url(r'z-posts', views.z_posts)
]