from django.conf.urls import url,include
from . import views
urlpatterns = [
	url(r'^$', views.faculty),
	url(r'apply/',views.applypage),
	url(r'cccc',views.checkapply),
	url(r'history',views.his),
	url(r'inprocess',views.inpro),
	url(r'approve',views.approved),
	url(r'help',views.help),
]