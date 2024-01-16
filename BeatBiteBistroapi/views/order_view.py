from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import Order, Customer, User
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
        if customer_order is not None:
            order = order.filter(customer_order_id=customer_order)
        if user_order is not None:
            order = order.filter(user_order_id=user_order)

        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def create(self, request):
        customer_name = request.data["customer_name"]
        customer_email = request.data["customer_email"]
        customer_phone = request.data["customer_phone"]
        # lookup customer by email
        customer = Customer.objects.get(email=customer_email)
        if customer is None:
            customer = Customer.objects.create(
                name=customer_name,
                email=customer_email,
                phone_number=customer_phone,
            )
        else:
            customer.name=customer_name
            customer.phone_number=customer_phone
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
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        order = Order.objects.get(pk=pk)

        order.order_date = request.data["order_date"]
        order.order_type = request.data["order_type"]
        order.payment_type = request.data["payment_type"]
        order.status = request.data["status"]
        order.tip_amount = request.data["tip_amount"]
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
