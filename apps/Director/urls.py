from django.conf.urls import url,include
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$',views.director),
	url(r'approve_dir/',views.approvepage_dir),
	url(r'viewdetails_dir/',views.singledetails_dir)	
	
	]
