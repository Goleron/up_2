from rest_framework import serializers
from shop.models import Order, OrderItem, Team, Category, Collection, Manufacturer, Product, Inventory, Review, Promotion

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'total_price', 'created_at', 'pickup_method']
        extra_kwargs = {'id': {'read_only': True}}

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']
        extra_kwargs = {'id': {'read_only': True}}

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'description', 'logo']
        extra_kwargs = {'id': {'read_only': True}, 'logo': {'required': False}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        extra_kwargs = {'id': {'read_only': True}}

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name', 'description', 'year']
        extra_kwargs = {'id': {'read_only': True}}

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']
        extra_kwargs = {'id': {'read_only': True}}

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'size', 'photo', 'create_date', 'is_available', 'category', 'team', 'collection', 'manufacturer']
        extra_kwargs = {
            'id': {'read_only': True},
            'photo': {'required': False},
            'create_date': {'read_only': True}
        }

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']
        extra_kwargs = {'id': {'read_only': True}}

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment', 'created_at']
        extra_kwargs = {'id': {'read_only': True}, 'created_at': {'read_only': True}}

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['name', 'discount_percent', 'start_date', 'end_date', 'products']
        extra_kwargs = {'id': {'read_only': True}}