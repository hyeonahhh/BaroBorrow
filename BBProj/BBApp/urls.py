from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, BarrowProductViewSet

product_router = SimpleRouter(trailing_slash=False)
product_router.register('products', ProductViewSet, basename='product')

barrowproduct_router = SimpleRouter(trailing_slash=False)
barrowproduct_router.register('barrowproducts', BarrowProductViewSet, basename='barrowproduct')

urlpatterns = [
    path('', include(product_router.urls)),
    path('products/<int:product_id>/', include(barrowproduct_router)),
]