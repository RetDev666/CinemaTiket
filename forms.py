from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'cinema']


class LoginForm:
    pass


class RegisterForm:
    pass


class BuyTicketForm:
    pass