from django.contrib import admin
from django.urls import path, include
from .views import RegisterVaccancy

app_name = "RegisterVaccancy"

urlpatterns = [
    
    path('', RegisterVaccancy, name = 'RegisterVaccancy'),

]
