from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def greet(request):
    message = '<h1>Hello world,django session</h1>'

    return httpresponse(message)
