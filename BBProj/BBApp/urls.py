from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from BBApp import views

from rest_framework.routers import SimpleRouter
from .views import ProductList, ProductDetail, ProductLikeDetail


urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/<int:pk>/like/', ProductLikeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
