from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Dryer, Laundry, UserProfile
from django.contrib.auth.forms import UserCreationForm

class LaundryForm(ModelForm):
    class Meta:
        model = Laundry
        fields = ['user', 'heaviness', 'cycle', 'mode']

class DryerForm(ModelForm):
    class Meta:
        model = Dryer
        fields = ['user', 'mode']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    floor_key = forms.IntegerField()

    class Meta:
        model = UserProfile
        fields = ('username', 'floor_key', 'email', 'password1', 'password2', )
