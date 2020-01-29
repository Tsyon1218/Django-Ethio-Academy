
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def RegisterVaccancy(request):
    return render (request, 'RegisterVaccancy/index.html')
