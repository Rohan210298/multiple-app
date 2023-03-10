from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse("Dhoni is the best finisher in the world")

def sachin(request):
    return HttpResponse("sachin is the god of cricket")