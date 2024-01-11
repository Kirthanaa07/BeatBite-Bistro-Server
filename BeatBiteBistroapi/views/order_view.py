from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Order, Customer, User
from BeatBiteBistroapi.serializers.all import OrderWithCustomerAndUserSerializer, OrderSerializer


class OrderView(ViewSet):
    def retrieve(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderWithCustomerAndUserSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        order = Order.objects.all()
        customer_order = request.query_params.get("customer_id", None)
        user_order = request.query_params.get("user_id", None)
        if customer_order is not None:
            order = order.filter(customer_order_id=customer_order)
        if user_order is not None:
            order = order.filter(user_order_id=user_order)

        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def create(self, request):
        customer_order = Customer.objects.get(pk=request.data["customer_id"])
        user_order = User.objects.get(pk=request.data["user_id"])

        order = Order.objects.create(
            order_date=request.data["order_date"],
            order_type=request.data["order_type"],
            payment_type=request.data["payment_type"],
            status=request.data["status"],
            customer=customer_order,
            tip_amount=request.data["tip_amount"],
            user=user_order,
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        order = Order.objects.get(pk=pk)
        

        customer_order = Customer.objects.get(pk=request.data["customer_id"])
        user_order = User.objects.get(pk=request.data["user_id"])
        order.order_date = request.data["order_date"],
        order.order_type = request.data["order_type"],
        order.payment_type = request.data["payment_type"],
        order.status = request.data["status"],
        order.customer = customer_order,
        order.tip_amount = request.data["tip_amount"],
        order.user = user_order,
        order.save()
        
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        
        order = Order.objects.get(pk=pk)
        order.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)



