from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello django')

def cat(request):
    return HttpResponse('Привет, котенок!')

def bithday(request):
    return HttpResponse('С днем рождения!')