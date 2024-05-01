from django.shortcuts import render
from rest_framework import generics
from market.models import Product
from market.serializers import ProductSerializer, ProductListing, ProductUpdate

# Create your views here.


class CreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInfo(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListingProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListing


class DeleteProduct(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdate
    lookup_field = "pk"

