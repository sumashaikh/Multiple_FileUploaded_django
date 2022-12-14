from django.urls import re_path
from . import views

app_name = "fileapp"

urlpatterns = [
    re_path(r'^$', views.BasicUploadView.as_view(), name='index'),
    re_path(r'^clear/$', views.clear_database, name='clear_database'),
]