from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=20)
    country_name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

class Element(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    element = models.CharField(max_length=20)

    def __str__(self):
        return self.element


class Entry(models.Model):
    date = models.DateField('Date')
    start = models.DateTimeField('Start Time')
    end = models.DateTimeField('End Time')
    duration = models.IntegerField()
    description = models.CharField(max_length=20)
    element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') # pylint: disable=maybe-no-member

class Account(models.Model):
    date = models.DateField('Date')
    act_type = models.CharField('Activity Type', max_length=6)
    act = models.IntegerField('Activity')
    wbs = models.CharField('WBS-Element', max_length=24)
    comment = models.CharField('Comment', max_length=20)
    hours = models.FloatField('Hours')

class Day(models.Model):
    date = models.DateField('Date')
    total_hours = models.FloatField('Total')
    tg1_hours = models.FloatField('Engineering')
    tg2_hours = models.FloatField('Sales')
    tg3_hours = models.FloatField('Unproductive')
    tg4_hours = models.FloatField('tbd')
    tg5_hours = models.FloatField('Training')
    tg6_hours = models.FloatField('tbd1')
    vac_hours = models.FloatField('Vacation')
    tg7_hours = models.FloatField('Sick')
    tg8_hours = models.FloatField('Research')
    target_hours = models.FloatField('Target')
    diff = models.FloatField('Difference')
    acc_target = models.FloatField('Accumulated Target')
    acc_total = models.FloatField('Accumulated Total')

    is_holiday = models.BooleanField('Public Holiday')
    is_weekend = models.BooleanField('Weekend')
    closed_sap = models.BooleanField('Closed in SAP')

    diff_sap = models.FloatField('Difference to SAP')
