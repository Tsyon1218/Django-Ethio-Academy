from django.contrib import admin
from django.urls import path, include
from .views import Contact

app_name = "Contact"

urlpatterns = [
    
    path('', Contact, name = 'Contact'),

]
