from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def register(request):
    return HttpResponse("Hello from registration page")


def all_products(request):
    all_p =Product.objects.all() #Template not done, 18:50 in lab 3, frontend work