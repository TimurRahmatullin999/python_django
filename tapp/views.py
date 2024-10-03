from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gh(request):
    return HttpResponse('gh-gh-gh')

def drive(request):
    return HttpResponse('врум-врум')

def evening(request):
    return HttpResponse('Добрый вечер!')