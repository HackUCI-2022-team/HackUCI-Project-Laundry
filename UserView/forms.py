from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Laundry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LaundryForm(ModelForm):
    class Meta:
        model = Laundry
        fields = ['heaviness', 'cycle']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid UCI email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

