from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Customer

class CustomerView(ViewSet):
  
  def retrieve(self, request, pk):
    
    customers = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(customers)
    return Response(serializer.data)
    
    
  def list(self, request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    customers = Customer.objects.create(
      name=request.data["name"],
      email=request.data["email"],
      phone_number=request.data["phone_number"]
    )
    
    serializer = CustomerSerializer(customers)
    return Response(serializer.data)
    
     
  
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ('id', 'name', 'email', 'phone_number') 
    depth = 1 