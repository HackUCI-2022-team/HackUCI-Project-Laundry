from django.contrib import admin
from .models import Laundry, Location, Dryer, Notification

# Register your models here.
admin.site.register(Laundry)
admin.site.register(Location)
admin.site.register(Dryer)
admin.site.register(Notification)