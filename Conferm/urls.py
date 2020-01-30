from django.contrib import admin
from django.urls import path, include
from .views import Conferm

app_name = "Conferm"

urlpatterns = [
    
    path('', Conferm, name = 'Conferm'),

]
