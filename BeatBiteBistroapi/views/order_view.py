from datetime import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from http import HTTPMethod
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Order, Customer, User
from BeatBiteBistroapi.models.items import Item
from BeatBiteBistroapi.models.order_items import OrderItem
from BeatBiteBistroapi.serializers.all import (
    OrderSerializer,
)


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
        user_order = request.query_params.get("user_id", None)
        order_status = request.query_params.get("status", None)
        if customer_order is not None:
            order = order.filter(customer_order_id=customer_order)
        if user_order is not None:
            order = order.filter(user_order_id=user_order)
        if order_status is not None:
            order = order.filter(status=order_status)

        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def create(self, request):
        customer_name = request.data["customer_name"]
        customer_email = request.data["customer_email"]
        customer_phone = request.data["customer_phone"]
        # lookup customer by email
        customer = Customer.objects.filter(name=customer_name).first()
        if customer is None:
            customer = Customer.objects.create(
                name=customer_name,
                email=customer_email,
                phone_number=customer_phone,
            )
        else:
            customer.name = customer_name
            customer.phone_number = customer_phone
            customer.save()

        user = User.objects.get(pk=request.data["user_id"])

        order = Order.objects.create(
            user=user,
            customer=customer,
            order_type=request.data["order_type"],
            order_date=request.data["order_date"],
            payment_type=request.data["payment_type"],
            status=request.data["status"],
            tip_amount=request.data["tip_amount"],
        )

        items = request.data["items"]
        for item in items:
            OrderItem.objects.create(
                order=Order.objects.get(pk=order.id),
                item=Item.objects.get(pk=item["id"]),
                quantity=item["quantity"],
            )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        order = Order.objects.get(pk=pk)

        orderId = request.data["id"]
        order.order_date = request.data["order_date"]
        order.order_type = request.data["order_type"]
        # https://www.w3schools.com/python/python_for_loops.asp
        if orderId is not None:
            orderItems = OrderItem.objects.filter(order_id=orderId)
            for orderItem in orderItems:
                orderItem.delete()

        items = request.data["items"]
        for item in items:
            OrderItem.objects.create(
                order=order,
                item=Item.objects.get(pk=item["id"]),
                quantity=item["quantity"],
            )

        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #https://www.django-rest-framework.org/api-guide/viewsets/
    @action(detail=True, methods=[HTTPMethod.POST])
    def close(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.status == 'Open':
            order.payment_type=request.data["payment_type"]
            order.status="Closed"
            order.tip_amount=request.data["tip_amount"]
            order.order_close_date=datetime.now()
        else:
            return Response({"message": "Order is already Closed."}, status=status.HTTP_400_BAD_REQUEST)
        
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
