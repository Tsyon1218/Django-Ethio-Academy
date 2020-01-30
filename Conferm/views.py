from django.shortcuts import render
from django.http import HttpResponse



def Conferm(request):
    return render (request, 'Conferm/index.html')