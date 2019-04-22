from django.test import TestCase,RequestFactory
from ..register.models import User,UserManager
from . import views as fac_views
from ..register import views as reg_views
from django.urls import reverse


class BlackCoxtesting(TestCase):
	def setUp(self):
		self.factory=RequestFactory()
		self.User = User.objects.create(first_name='Testname',last_name='last',password='Checkpasswd',email='gywg@gmail.com',u_type='faculty')

	def test_redirect(self):
		request = self.factory.get('/faculty/')
		request.User = self.User
		#request.session['id'] = self.User.email
		response = fac_views.faculty(request)
		self.assertEqual(response.status_code, 200)
