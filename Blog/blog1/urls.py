from django.contrib import admin
from django.urls import path
from blog1.views import home_view

urlpatterns = [
    path("",home_view, name="home"),
]
