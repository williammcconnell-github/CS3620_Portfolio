from django.shortcuts import render, redirect
from .models import Hobby
from .models import Portfolio, Contact
from .forms import PortfolioForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


@login_required
def create_portfolio(request):
    form = PortfolioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolios')
    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form})


@login_required
def update_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    form = PortfolioForm(request.POST or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolios')
    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form, 'portfolio': portfolio})


@login_required
def delete_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('PortfolioDatabase:portfolios')
    return render(request, 'PortfolioDatabase/portfolio-delete.html', {'portfolio': portfolio})


def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'PortfolioDatabase/portfolioDetail.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Message Sent.')
        return redirect('PortfolioDatabase:home')
    return render(request, 'PortfolioDatabase/contact.html', {'form': form})
