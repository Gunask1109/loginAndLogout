from django.contrib import admin
from django.urls import path, include
from user import views
urlpatterns = [

    path('', views.index, name="home"),
    path('login', views.loginUser, name="loginUser"),
    path('logoutUser', views.logoutUser, name="logoutUser"),
]
