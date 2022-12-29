from django.urls import re_path as url

from basic.dlearn.dc_gan import views

urlpatterns = [
    url(f'fake-faces', views.fake_faces)
]