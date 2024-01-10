from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Item

class ItemView(ViewSet):
  
  def retrieve(self, request, pk):
    
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
    
    
  def list(self, request):
    
    item = Item.objects.all()
    serializer = ItemSerializer(item, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    item = Item.objects.create(
      name=request.data["name"],
      price=request.data["price"]
    )
    serializer = ItemSerializer(item)
    return Response(serializer.data)
  
class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ('id', 'name', 'price')  