from django.contrib import admin
from django.urls import path, include
from .views import About

app_name = "About"

urlpatterns = [
    
    path('', About, name = 'About'),

]
