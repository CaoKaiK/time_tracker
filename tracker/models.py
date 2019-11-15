from django.db import models

# Create your models here.

class entries(models.Model):
    date = models.DateField('Date')
    start = models.DateTimeField('Start Time')
    end = models.DateTimeField('End Time')
    duration = models.ImageField()

