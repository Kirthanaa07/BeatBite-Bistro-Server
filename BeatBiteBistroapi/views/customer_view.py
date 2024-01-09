from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Customer

class CustomerView(ViewSet):
  
  def retrieve(self, request, pk):
    
    customer = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)
    
    
  def list(self, request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)
  
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ('id', 'name', 'email', 'phone_number') 
    depth = 1 