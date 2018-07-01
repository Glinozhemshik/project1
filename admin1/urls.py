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