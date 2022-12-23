from django.urls import re_path as url  # re_path는 path 뒤에 추가로 붙는 경로를 뜻한다.

from nlp.samsung_report import views as samsung_report_views

urlpatterns = [
    url(r'samsung-report', samsung_report_views.samsung_report),  # GET
]