from django.db import models

# Create your models here.
from ..register import models

class Leaves(models.Model):
	email = models.CharField(max_length=255)
	leave_type = models.CharField(max_length=255)
	from_date = models.DateTimeField()
	to_date = models.DateTimeField()
	


#class Faculty