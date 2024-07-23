from django.shortcuts import render
from django.http import HttpResponse

def idle(request):
    return HttpResponse("Hello Brother")

# Create your views here.
