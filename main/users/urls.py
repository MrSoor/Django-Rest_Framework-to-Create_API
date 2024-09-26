from django.urls import path
from .views import UserDetail,UserList,ProductDetail,ProductList

urlpatterns = [
    path('users/', UserList.as_view(),name='Users'),
    path('user/<int:pk>', UserDetail.as_view(),name='User'),
    path('products/', ProductList.as_view(),name='Products'),
    path('product/<int:pk>', ProductDetail.as_view(),name='Product'),
]
