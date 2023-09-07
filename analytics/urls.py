from django.urls import re_path
from .views import *

app_name = 'analytics'

urlpatterns = [
    re_path(r'^$', Homeanalytics, name='center-home'),
]
