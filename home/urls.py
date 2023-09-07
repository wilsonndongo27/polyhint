from django.urls import re_path
from home.views import *

app_name = 'home'

urlpatterns = [
    re_path(r'^$', HomeView, name='home')
]