from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('HELLO THIS IS A VIEW IN MY_APP...with some extra text now')
