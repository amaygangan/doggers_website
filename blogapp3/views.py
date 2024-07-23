from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Hello,Welcome to ba3")

def contact(request):
    return HttpResponse("I'm in ba3")

def job(request):
    return HttpResponse("I'm a good Python Programmer and Web Developer")

# Create your views here.
