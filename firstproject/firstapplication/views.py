from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("Hello, This is the first application")

def hi(request):
    return render(request,"hi.html")

