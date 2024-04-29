from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('register/', register, name = 'register'),
    path('login/', Login, name = 'login'), 
    path('add/', addproduct, name = 'add'),
]