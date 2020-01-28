from django.shortcuts import render
from django.http import HttpResponse




def Contact(request):
    return render (request, 'Contact/Contact.html')