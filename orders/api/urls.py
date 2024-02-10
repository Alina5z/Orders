from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('orders/', views.OrdersList.as_view()),
    path('orders/<int:pk>', views.OrderDetail.as_view()),
    path('products/', views.ProductsList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('prodinorders/', views.ProductsInOrdersList.as_view()),
    path('prodinorders/<int:pk>', views.ProductsInOrdersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
