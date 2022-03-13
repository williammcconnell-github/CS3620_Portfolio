from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name='hobbyDetail'),
    path('portfolios/', views.portfolios, name="portfolios"),
    path('portfolios/<int:portfolio_id>', views.portfolio_detail, name='portfolioDetail'),
    path('contact/', views.contact, name="contact")
]
