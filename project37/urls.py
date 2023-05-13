"""project37 URL Configuration

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
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Fbv_string',Fbv_string, name='Fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(), name='Cbv_string'),

    path('Fbv_html/',Fbv_html, name='Fbv_html'),
    path('Cbv_html/',Cbv_html.as_view(), name='Cbv_html'),

    path('Fbv_forms/',Fbv_forms, name='Fbv_forms'),
    path('Cbv_forms/',Cbv_forms.as_view(), name='Cbv_forms'),


]
