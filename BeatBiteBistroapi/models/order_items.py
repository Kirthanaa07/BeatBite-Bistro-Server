from django.db import models
from .orders import Order
from .items import Item

class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name="orderitems", on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name="items")
  quantity = models.IntegerField()