from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        if postData['user_type']!="faculty" and postData[user_type]!="director" and postData[user_type]!="hod":
            errors['user_type'] = "Not valid User Type!"
                    
        return errors

class User(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    email       = models.CharField(max_length=255,primary_key=True,unique=True)
    password    = models.CharField(max_length=255)
    user_type   = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    objects     = UserManager()
    n_casualleave=models.IntegerField(default=30)
    u_casualleave=models.IntegerField(default=0)
    n_commutingleave=models.IntegerField(default=30)
    u_commutingleave=models.IntegerField(default=0)
    n_specialleave=models.IntegerField(default=30)
    u_specialleave=models.IntegerField(default=0)
    n_Earnleave=models.IntegerField(default=30)
    u_Earnleave=models.IntegerField(default=0)
    n_paternityleave=models.IntegerField(default=30)
    u_paternityleave=models.IntegerField(default=0)
    n_HalfDayleave=models.IntegerField(default=30)
    u_HalfDayleave=models.IntegerField(default=0)
    n_Dutyleave=models.IntegerField(default=30)
    u_Dutyleave=models.IntegerField(default=0)
    n_sickleave=models.IntegerField(default=30)
    u_sickleave=models.IntegerField(default=0)
    n_maternityleave=models.IntegerField(default=30)
    u_maternityleave=models.IntegerField(default=0)
    
