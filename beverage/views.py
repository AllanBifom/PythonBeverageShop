from django.shortcuts import render
from django.http import HttpResponse
from .models import Beverage


def home(request):
    beverage = Beverage.objects.all()
    return render(request, 'homePage.html', {'beverage': beverage})
