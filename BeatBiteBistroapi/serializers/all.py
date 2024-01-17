from rest_framework import serializers
from BeatBiteBistroapi.models import User, Order, Customer, Item, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "name", "email", "phone_number")
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "uid", "name", "image", "role")


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "price")


class OrderItemsSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = OrderItem
        fields = ("id", "item", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    user = UserSerializer()
    items = OrderItemsSerializer(many=True, source="orderitems", read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "customer",
            "items",
            "order_date",
            "payment_type",
            "order_type",
            "tip_amount",
            "status",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    item = ItemSerializer()

    class Meta:
        model = OrderItem
        fields = ("id", "order", "item", "quantity")
