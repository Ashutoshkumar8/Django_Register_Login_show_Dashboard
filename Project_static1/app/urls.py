from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name="register"), 
    path('login/',login,name="login"),
    path('login1/',login1,name="login1"),
    #path('logout/',logout,name="logout") 
]