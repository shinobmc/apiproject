from django.db import models

# Create your models here.

class SignupDetails(models.Model):
    f_name = models.CharField(max_length = 30)
    l_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 30)