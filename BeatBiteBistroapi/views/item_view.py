from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Item
from BeatBiteBistroapi.serializers.all import ItemSerializer

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
  
  def update(self, request, pk):
    
    item = Item.objects.get(pk=pk)
    item.name = request.data["name"]
    item.price = request.data["price"]
    item.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)  
 