from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def luck(request):
    return HttpResponse('Удачи тебе!')

def allright(request):
    return HttpResponse('Все правильно!')

def lazy(request):
    return HttpResponse('You are so lazy')