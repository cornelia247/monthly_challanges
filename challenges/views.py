from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Learn Everything about Django")

def febuary(request):
    return HttpResponse("Learn how to be Origanised")