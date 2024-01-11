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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "item", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "customer",
            "order_date",
            "payment_type",
            "order_type",
            "tip_amount",
            "status",
        )


class OrderWithCustomerAndUserSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "customer",
            "order_date",
            "order_type",
            "tip_amount",
            "status",
            "payment_type",
        )
