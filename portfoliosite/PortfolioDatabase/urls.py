from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="hobbyDetail"),
    path('portfolios/', views.portfolios, name="portfolios"),
    path('portfolios/add', views.create_portfolio, name="create_portfolio"),
    path('portfolios/update/<int:portfolio_id>', views.update_portfolio, name="update_portfolio"),
    path('portfolios/delete/<int:portfolio_id>', views.delete_portfolio, name="delete_portfolio"),
    path('portfolios/<int:portfolio_id>', views.portfolio_detail, name="portfolioDetail"),
    path('contact/', views.contact, name="contact")
]
