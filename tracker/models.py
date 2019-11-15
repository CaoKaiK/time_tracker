from django.db import models

# Create your models here.

class Entry(models.Model):
    date = models.DateField('Date')
    start = models.DateTimeField('Start Time')
    end = models.DateTimeField('End Time')
    duration = models.IntegerField()
    description = models.CharField(max_length=20)

