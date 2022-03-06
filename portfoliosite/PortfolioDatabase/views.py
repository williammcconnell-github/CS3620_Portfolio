from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolio


# Create your views here.
def home(request):
    return HttpResponse("<h1>Home</h1>"
                        "<p>Welcome to my home page</p>"
                        "<p>My name is William McConnell. I am a 29 year old CS student looking to graduate and move "
                        "into the work force as of the end of this spring.</p>")


def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def contact(request):
    return HttpResponse("williammcconnell@mail.wsu.edu")
