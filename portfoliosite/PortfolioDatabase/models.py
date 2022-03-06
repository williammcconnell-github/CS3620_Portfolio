from django.db import models

# Create your models here.


class Hobby(models.Model):
    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)


class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)
