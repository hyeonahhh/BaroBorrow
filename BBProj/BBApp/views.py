from datetime import datetime
from django.shortcuts import render, redirect
from carton.cart import Cart
from .models import Product, BarrowProduct
from django.http import HttpResponse
from .serializers import ProductSerializer, BarrowProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def add_cart(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(id=product_id)
    price = product.rental_fee
    cart.add(product, price)
    return redirect('show_cart')

def show_cart(request):
    return render(request, '')

def remove_cart(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect('show_cart')



def home(request):
    products = Product.objects.filter()
    return render(request, '')

class ProductLikeDetail(APIView):
    def productlike(self, request, pk):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, pk=pk)
            if product.like_users.filter(pk=request.user.pk).exists():
                product.like_users.remove(request.user)
                product.save()
            else:
                product.like_users.add(request.user)
                product.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):
    def get(self, request): #물품 목록들 조회
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)
    
    def post(self, request): #빌려주기 작성
        serializer = ProductSerializer(data=request.data)
        serializer.owner = request.user
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, pk):
        product = get_object_or_404(Product, pk=pk)
        return product

    def get(self, request, pk): #디테일뷰
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk): #삭제
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class BarrowProductList(APIView):
    def post(self, request):
        serializer = BarrowProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        queryset = BarrowProduct.objects.all()
        serializer = BarrowProductSerializer(queryset, many=True)
        return Response(serializer.data)

class BarrowProductDetail(APIView):
    def get_object(self, pk):
        if BarrowProduct.barrow_end < datetime.date.today():
            BarrowProduct.is_activate = False
        
        try:
            return BarrowProduct.objects.get(pk=pk)
        except BarrowProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        borrow_product = self.get_object(pk)
        serializer = BarrowProductSerializer(borrow_product)
        return Response(serializer.data)







    







