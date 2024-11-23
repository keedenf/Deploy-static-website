from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('register_user/', views.register_user, name='register_user'),
]