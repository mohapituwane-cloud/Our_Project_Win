from django.shortcuts import render 
from django.http import HttpResponse


def page1(request):
    return render(request, 'index.html')

