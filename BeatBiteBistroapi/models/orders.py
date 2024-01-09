from django.db import models
from .customers import Customer
from .user import User
# from .BeatBiteBistroapi.models.items import Item

class Order(models.Model):
  
  uid = models.ForeignKey(User, on_delete=models.CASCADE)
  customers = models.ForeignKey(Customer, on_delete= models.CASCADE)
  order_date = models.DateTimeField()
  payment_type = models.CharField(max_length=50)
  order_type = models.CharField(max_length=50)
  tip_amount = models.IntegerField()
  status = models.CharField(max_length=5) 
  
  # item = models.ManyToManyField(Item, through="orderitem", related_name="order")