from Sepatu.models import Product,Customer,Order,OrderItem,Payment
from rest_framework import serializers

class ProductSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'        

class OrderSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerealizer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'