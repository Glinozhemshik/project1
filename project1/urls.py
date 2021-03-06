"""Test_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from admin1.views import *

urlpatterns = [
    path('admin/', admins),
    path('admin1/', form_set),
    path('', main_page),
    re_path('^element/(?P<x>\w+)/$', cnt),
    re_path('^articles/(?P<x>\w+)/$', cnt),
    path('admin/articles/add/', add),
    path('admin/articles', articles),
    re_path('^admin/articles_del/(?P<content>\w+)/$', articles_del),
    re_path('^admin/articles/edit/(?P<slug>\w+)/$', articles_edit),
    path('accounts/', include('allauth.urls')),
    path('admins/', admin.site.urls),

]