from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100,default='event')
    description = models.TextField(default='')
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)


