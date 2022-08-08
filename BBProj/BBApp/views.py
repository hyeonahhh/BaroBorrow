from django.shortcuts import render
from carton.cart import Cart
from .models import Product, BarrowProduct
from django.http import HttpResponse
from .serializers import ProductSerializer, BarrowProductSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BarrowProductViewSet(ModelViewSet):
    queryset = BarrowProduct.objects.all()
    serializer_class = BarrowProductSerializer
