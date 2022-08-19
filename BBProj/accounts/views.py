from re import search
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .serializers import AccountSerializer, UserLocationSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from accounts import serializers
from rest_framework.generics import get_object_or_404


@csrf_exempt
def account_list(request):
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = AccountSerializer(query_set, many=True)
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':serializer}, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def account(request, pk):
    obj = User.objects.get(pk=pk)

    if request.method =='GET':
        serializer = AccountSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_username = data['data']['username']
        obj  = User.objects.get(username=search_username)
        serializer = AccountSerializer(obj)
        if data['data']['password'] == obj.password:
            return JsonResponse(serializer.data, status=200)
        else:
            return HttpResponse(status=400)

class BorrowLocation(APIView):
    def post(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserLocationSerializer(user, data=request.data)
       # print(user)
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)