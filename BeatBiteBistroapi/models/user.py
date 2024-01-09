from django.db import models

class User(models.Model):
  
  uid = models.CharField(max_length=50)
  name = models.CharField(max_length=50, default='John Doe')
  image = models.ImageField(max_length=50, default='default_image.jpg')
  role = models.CharField(max_length=50, default='Cashier')
  