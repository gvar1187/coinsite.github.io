from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta(): 
        model = User
        fields = ['email', 'password1', 'password2']