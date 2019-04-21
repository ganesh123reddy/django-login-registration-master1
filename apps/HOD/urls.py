from django.conf.urls import url,include
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.hod),
	url(r'approve',views.approvepage),
	url(r'approvecheck',views.approvecheck),
	#url(r'viewdetails',views.singledetails)
]