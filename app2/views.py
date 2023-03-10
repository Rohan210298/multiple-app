from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse("virat is the best batsman in the world")

def abd(request):
    return HttpResponse("abd is know as mr 360")