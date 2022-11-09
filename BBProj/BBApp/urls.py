from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from BBApp import views

from rest_framework.routers import SimpleRouter
from .views import NotBarrowedProductList, ProductList, ProductDetail, ProductLikeDetail, ProductViewSet

from rest_framework.routers import SimpleRouter

product_router = SimpleRouter(trailing_slash=False)
product_router.register('products', ProductViewSet, basename='product')


urlpatterns = [
    path('product/', ProductList.as_view()),
    path('nbproduct/', NotBarrowedProductList.as_view()),
    path('today_available/', views.TodayAvailableList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/<int:pk>/like/', ProductLikeDetail.as_view()),
    path('product/<int:pk>/borrow/', views.CreateBarrowProduct.as_view()), #빌리기
    path('barrowedinfo/<int:pk>/', views.BarrowedInfoList.as_view()),
    path('mypage/borrow/', views.MyBarrowProductList.as_view()),
    path('mypage/myproduct/', views.MyProductList.as_view()),
    path('mypage/likeproducts/', views.ProductLikeList.as_view()),
    path('mypage/reviewresult/', views.MyReviewResult.as_view()),
    path('search/', include(product_router.urls)),
    path('return/<int:pk>/', views.ReturnProduct.as_view()),
    path('review/<int:pk>/', views.LeaveReview.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
