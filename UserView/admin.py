from django.contrib import admin
from .models import Laundry, Dryer, Notification, Floor

# Register your models here.
admin.site.register(Laundry)
admin.site.register(Dryer)
admin.site.register(Notification)
admin.site.register(Floor)