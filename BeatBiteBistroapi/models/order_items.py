from django.db import models
from .orders import Order
from .items import Item

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()