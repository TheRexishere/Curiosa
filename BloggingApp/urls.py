from django.contrib import admin
from django.urls import path, include
from BloggingApp import views

urlpatterns = [
    path('', views.home, name="")
]
