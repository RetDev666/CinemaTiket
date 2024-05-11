from django import forms
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'cinema']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class BuyTicketForm:
    pass