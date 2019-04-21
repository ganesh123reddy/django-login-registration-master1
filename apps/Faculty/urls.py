from django.conf.urls import url,include
from . import views
urlpatterns = [
	url(r'^$', views.faculty),
	url(r'apply/',views.applypage),
	url(r'cccc',views.checkapply)
]