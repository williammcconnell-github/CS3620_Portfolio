from django.shortcuts import render
from .models import Hobby
from .models import Portfolio


# Create your views here.
def home(request):
    context = {}
    return render(request, 'PortfolioDatabase/home.html', context)


def hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'PortfolioDatabase/hobbies.html', context)


def hobby_detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'PortfolioDatabase/hobbyDetail.html', context)


def portfolios(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'PortfolioDatabase/portfolios.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'PortfolioDatabase/portfolioDetail.html', context)


def contact(request):
    context = {}
    return render(request, 'PortfolioDatabase/contact.html', context)
