from django.contrib import admin
from .models import Laundry, Dryer, Notification, Floor, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Laundry)
admin.site.register(Dryer)
admin.site.register(Notification)
admin.site.register(Floor)
admin.site.register(UserProfile, UserAdmin)