from django import forms
from .models import Portfolio, Contact


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name', 'portfolio_desc', 'portfolio_image']


class ContactForm(forms.ModelForm):
    contact_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_email = forms.EmailField(max_length=300, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contact_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_email', 'contact_message')

