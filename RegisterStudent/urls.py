from django.contrib import admin
from django.urls import path, include
from .views import RegisterStudent

app_name = "RegisterStudent"

urlpatterns = [
    
    path('', RegisterStudent, name = 'RegisterStudent'),

]
