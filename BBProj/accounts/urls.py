from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('accounts/', views.account_list),
    path('accounts/<int:pk>/', views.account),
    path('login/', views.login),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('location/', views.BorrowLocation.as_view()),
 ]
