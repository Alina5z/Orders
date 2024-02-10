from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Orders, Products, ProductsInOrders


class ProdInOrderSerialize(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ProductsInOrders
        fields = ['id', 'order', 'prod', 'quantite', 'price', 'owner']


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['id', 'created', 'status', 'owner']


class ProductsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Products
        fields = ['id', 'title', 'owner']


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders', 'products']
