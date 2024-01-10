from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Order, Customer
from BeatBiteBistroapi.views.customer_view import CustomerSerializer


class OrderView(ViewSet):
    def retrieve(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        order = Order.objects.all()
        customer_order = request.query_params.get("customer_id", None)
        if customer_order is not None:
            order = order.filter(customer_order_id=customer_order)

        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
    
    def create(self, request):
      customer_order = Customer.objects.get(pk=request.data["customer_id"])
    
      order = Order.objects.create(
        order_date=request.data["order_date"],
        order_type=request.data["order_type"],
        payment_type=request.data["payment_type"],
        status=request.data["status"],
        customers=customer_order,
        tip_amount=request.data["tip_amount"]
        
      )
      serializer = OrderSerializer(order)
      return Response(serializer.data,status=status.HTTP_201_CREATED)


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Order
        fields = (
            "id",
            "uid",
            "customer",
            "order_date",
            "payment_type",
            "order_type",
            "tip_amount",
            "status",
        )
