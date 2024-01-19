from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Customer
from BeatBiteBistroapi.serializers.all import CustomerSerializer

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
  
  def update(self, request, pk):
    
    customer = Customer.objects.get(pk=pk)
    customer.name = request.data["name"]
    customer.email = request.data["email"]
    customer.phone_number = request.data["phone_number"]
    customer.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  
  def destroy(self, request, pk):
    
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT) 
     
  
