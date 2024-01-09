from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import OrderItem


class OrderItemView(ViewSet):
  
    def retrieve(self, request, pk):
      
        order_item = OrderItem.objects(pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def list(self, request):
      
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many=True)
        return Response(serializer.data)
      
class OrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    
    model = OrderItem
    fields = ('id', 'order', 'item', 'quantity') 

        
        
