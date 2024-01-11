from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from BeatBiteBistroapi.models import OrderItem, Order, Item
from BeatBiteBistroapi.serializers.all import OrderItemSerializer


class OrderItemView(ViewSet):
    def retrieve(self, request, pk):
        try:
            order_item = OrderItem.objects(pk=pk)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        except OrderItem.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many=True)
        return Response(serializer.data)

    def create(self, request):
        item = Item.objects.get(pk=request.data["item_id"])
        order = Order.objects.get(pk=request.data["order_id"])

        order_item = OrderItem.objects.create(
            item=item, order=order, quantity=request.data["quantity"]
        )
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def update(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)

        quantity = request.data["quantity"]
        order_item.quantity = quantity

        order_item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
