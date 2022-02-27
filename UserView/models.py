from random import choice
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver

# Create your models here
class Floor(models.Model):
    floor_key = models.IntegerField()

class UserProfile(AbstractUser):
    floor_key = models.IntegerField(null=True)

class Laundry(models.Model):
    heaviness_choices = [
        ('light', 'LIGHT'),
        ('medium', 'MEDIUM'),
        ('heavy', 'HEAVY'),
        ('off', 'OFF')
    ]

    cycle_choices = [
        ('normal', 'NORMAL'),
        ('delicate', 'DELICATE'),
        ('perm', 'PERM'),
        ('off', 'OFF')
    ]

    mode_choices = [
        ('free', 'FREE'),
        ('occupied', 'OCCUPIED'),
        ('neutral', 'NEUTRAL')
    ]

    heaviness = models.CharField(choices=heaviness_choices, max_length=6, default='off')
    cycle = models.CharField(choices=cycle_choices, max_length=8, default='off')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    mode = models.CharField(choices=mode_choices, max_length=8, default='neutral')
    floor_key = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Laundry on " + str(self.floor_key)

class Dryer(models.Model):
    mode_choices = [
        ('free', 'FREE'),
        ('occupied', 'OCCUPIED'),
        ('neutral', 'NEUTRAL')
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    mode = models.CharField(choices=mode_choices, max_length=8, default='neutral')
    floor_key = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Dryer on " + str(self.floor_key)

class Notification(models.Model):
    recipient = models.ManyToManyField(UserProfile)
    message = models.TextField()
    sent_date = models.DateTimeField()

    def __str__(self) -> str:
        return "Message To: " + self.recipient.username
