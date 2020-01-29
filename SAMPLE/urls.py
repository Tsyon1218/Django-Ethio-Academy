from django.contrib import admin
from django.urls import path, include
from .views import SAMPLE

app_name = "SAMPLE"

urlpatterns = [
    
    path('', SAMPLE, name = 'SAMPLE'),

]
