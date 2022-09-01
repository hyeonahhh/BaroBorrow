from datetime import datetime, date, timedelta
from django.utils.dateformat import DateFormat
from django.shortcuts import render, redirect
from .models import Product, BarrowProduct
from django.http import HttpResponse
from .serializers import ProductLikeSerializer, ProductSerializer, BarrowProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from accounts.models import User

# Create your views here.

def home(request):
    products = Product.objects.filter()
    return render(request, '')

class ProductLikeDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        username = request.GET.get('username', None)
        obj  = User.objects.get(username=username)
        if product.like_users.filter(pk=obj.pk).exists():
            product.like_users.remove(obj)
            product.save()
        else:
            product.like_users.add(obj)
            product.save()
        serializer = ProductLikeSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotBarrowedProductList(APIView):
    def get(self, request):
        products = Product.objects.filter(is_barrowed=False).all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)


class ProductList(APIView):
    def get(self, request, format=None): #물품 목록들 조회
        products = Product.objects.filter(barrow_available_end__range=[date.today(), date.today() + timedelta(weeks=500)]).values().all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)
    
    def post(self, request): #빌려주기 작성
        print(request.data['owner']['username'])
        obj  = User.objects.get(username=request.data['owner']['username'])
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodayAvailableList(APIView):
    def get(self, request, format=None): #물품 목록들 조회
        products = Product.objects.filter(barrow_available_start__range=[date.today() - timedelta(weeks=500), date.today()]).values().all()
        products = products.filter(barrow_available_end__range=[date.today(), date.today() + timedelta(weeks=500)]).values().all()
        products = products.filter(is_barrowed = False)
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)


class ProductDetail(APIView):
    def get_object(self, pk):
        product = get_object_or_404(Product, pk=pk)
        return product

    def get(self, request, pk, format=None): #디테일뷰
        product = self.get_object(pk)
        serializer = ProductLikeSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk, format=None): #삭제
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class CreateBarrowProduct(APIView):
    def post(self, request, pk): #빌리기 정보 저장
        print(request.data['user']['username'])
        obj  = User.objects.get(username=request.data['user']['username'])
        serializer = BarrowProductSerializer(data=request.data)
        product = get_object_or_404(Product, pk=pk)
        serializer.product = product.id
        print(serializer)
        if serializer.is_valid():
            serializer.save(user=obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#빌린 내역 - 수정필요
class MyBarrowProductList(APIView):
    def get(self, request): 
        username = request.GET.get('username', None)
        obj  = User.objects.get(username=username)
        queryset = BarrowProduct.objects.filter(user=obj)
        serializer = BarrowProductSerializer(queryset, many=True)
        return Response(serializer.data)

#빌려준 내역
class MyProductList(APIView):
    def get(self, request):
        username = request.GET.get('username', None)
        obj  = User.objects.get(username=username)
        queryset = Product.objects.filter(owner = obj)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class MyBarrowProductDetail(APIView):
    def get_object(self, pk):
        try:
            return BarrowProduct.objects.get(pk=pk)
        except BarrowProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk): #내 바로 내역 - 디테일
        borrow_product = self.get_object(pk)
        serializer = BarrowProductSerializer(borrow_product)
        return Response(serializer.data)

#검색
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter]
    search_fields = ('product_name',)

#반납
class ReturnProduct(APIView):
    def get_object(self, pk):
        product = get_object_or_404(BarrowProduct, pk=pk)
        return product

    def get(self, request, pk): #디테일뷰
        product = self.get_object(pk)
        username = request.GET.get('username', None)
        obj  = User.objects.get(username=username)
        if (product.user == obj):
            product.is_return = True
            product.product.is_barrowed = False
            serializer = BarrowProductSerializer(product)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        




    







