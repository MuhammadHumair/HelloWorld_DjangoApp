from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Django...!!!")


def profile(request):
    return HttpResponse("Profile Page...!!!")

