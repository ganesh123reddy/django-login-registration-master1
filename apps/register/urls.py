from django.conf.urls import url,include
from . import views
from django.contrib import admin
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'faculty/',include('apps.Faculty.urls')),
    url(r'hod/',include('apps.HOD.urls')),
    url(r'admin/', admin.site.urls)
]