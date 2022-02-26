from django.db import models
from django.forms import ModelForm
from .models import Laundry, Location

class LaundryForm(ModelForm):
    class Meta:
        model = Laundry
        fields = ['heaviness', 'cycle']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['dorm', 'floor']