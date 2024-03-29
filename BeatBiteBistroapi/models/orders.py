from django.db import models

from BeatBiteBistroapi.models.items import Item
from .customers import Customer
from .user import User
# from .BeatBiteBistroapi.models.items import Item

class Order(models.Model):
  
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
  customer = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name='orders')
  order_date = models.DateTimeField()
  order_close_date = models.DateTimeField(null=True)
  payment_type = models.CharField(max_length=50, blank=True, default='')
  order_type = models.CharField(max_length=50)
  tip_amount = models.IntegerField()
  status = models.CharField(max_length=5) 
  items = models.ManyToManyField(Item, through="orderitem", related_name="orders")