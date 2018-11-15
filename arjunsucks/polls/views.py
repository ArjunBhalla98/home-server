from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Self note: Views are 'view functions', which take an HTTP req and return an
# HTTP response.


def index(request):
    return HttpResponse("Hello World. You're at the polls index.")
