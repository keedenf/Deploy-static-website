from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add_cart/<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]