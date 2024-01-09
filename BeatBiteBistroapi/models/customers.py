from django.db import models

class Customer(models.Model):
  
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  phone_number = models.IntegerField()