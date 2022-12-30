from django.urls import re_path as url
from blog.posts import views

urlpatterns = [
    url(r'b-post$', views.b_post),
    url(r'b-post-list', views.b_post_list)
]