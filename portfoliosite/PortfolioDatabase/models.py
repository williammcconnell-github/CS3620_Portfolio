from django.db import models

# Create your models here.


class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://cdn.iconscout.com/icon/premium/png-256-thumb/hobby-6-1100854.png")


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500, default="https://cdn.iconscout.com/icon/premium/png-256-thumb/notebook-1717991-1459674.png")


class Contact(models.Model):

    def __str__(self):
        return self.contact_name

    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=300)
    contact_message = models.TextField(max_length=1000)
