from django.urls import re_path as url
from blog.b_users import views

urlpatterns = [
    url(r'b-user$', views.b_user),
    url(r'b-user-list', views.b_user_list),
    url(r'login-buser', views.login_buser),
]