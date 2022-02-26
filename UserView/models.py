from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Laundry(models.Model):
    heaviness_choices = [
        ('light', 'LIGHT'),
        ('medium', 'MEDIUM'),
        ('heavy', 'HEAVY')
    ]

    cycle_choices = [
        ('normal', 'NORMAL'),
        ('delicate', 'DELICATE'),
        ('perm', 'PERM')
    ]

    heaviness = models.CharField(choices=heaviness_choices, max_length=6)
    cycle = models.CharField(choices=cycle_choices, max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mode = models.BooleanField()

    def __str__(self) -> str:
        return self.user + "'s Laundry Machine"

class Location(models.Model):
    dorm_choices = [
        ('mesa', 'MESA'),
        ('middle earth', 'MIDDLE EARTH')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dorm = models.CharField(choices=dorm_choices, max_length=12)
    #hall 
    floor = models.IntegerField()

    def __str__(self) -> str:
        return self.user + "'s Location"

class Dryer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mode = models.BooleanField()

    def __str__(self) -> str:
        return self.user + "'s Dryer Machine"

class Notification(models.Model):
    recipient = models.ManyToManyField(User)
    message = models.TextField()
    sent_date = models.DateTimeField()

    def __str__(self) -> str:
        return "Message To: " + self.recipient.username

