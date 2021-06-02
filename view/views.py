
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    all = display.objects.all()

    return  render(request,"users/index.html",{
        "display":all
    })
