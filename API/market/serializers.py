from rest_framework import serializers
from market.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "category"]


class ProductListing(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]


class ProductUpdate(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["stock"]
