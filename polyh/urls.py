"""polyh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from core import urls as core_urls
from api import urls as api_urls
from analytics import urls as analytics_urls

urlpatterns = [
    path('', include(home_urls, namespace='polyh')),
    path('core', include(core_urls, namespace='core')),
    path('api', include(home_urls, namespace='api')),
    path('solution-center', include(analytics_urls, namespace='solution-center')),
    
    path('polyh-super-admin/', admin.site.urls),
]
