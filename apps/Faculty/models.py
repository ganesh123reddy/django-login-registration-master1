from __future__ import unicode_literals
from django.db import models


# Create your models here.

#from ..register import models

class Leaves(models.Model):
	email = models.CharField(max_length=255)
	leave_type = models.CharField(max_length=255)
	from_date = models.DateTimeField()
	to_date = models.DateTimeField()
	status = models.IntegerField(default=3)#2- HOD Accepted #1 Director Accepted #0 for any rejection



#class Faculty