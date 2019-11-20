from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=20, help_text="Internal Project Name")
    country_name = models.CharField(max_length=30, help_text="Country of Customer/Project")
    customer_name = models.CharField(max_length=30, blank=True, null=True, help_text="Customer Name")
    customer_street = models.CharField(max_length=50, blank=True, null=True, help_text="Customer Address Street")
    customer_postal = models.CharField(max_length=15, blank=True, null=True, help_text="Customer Postal Code")
    customer_city = models.CharField(max_length=30, blank=True, null=True, help_text="Customer City")

    active = models.BooleanField(default=True, help_text="Project is still active")

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_subfeature_elements(self):
        return self.element_set.filter(project_id = self.id) # pylint: disable=maybe-no-member

    def __str__(self):
        return self.project_name

class Element(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    element = models.CharField(max_length=24, help_text='WBS/PSP-Element')
    act_description = models.CharField(max_length=20, help_text="Describes the general activity for this WBS/PSP")
    act_type = models.CharField('Activity Type', max_length=6, help_text="Activity Type for this WBS/PSP")
    act = models.IntegerField('Activity', help_text="Activity Type for this WBS/PSP")
    

    def __str__(self):
        return self.element


class Entry(models.Model):
    date = models.DateField('Date')
    start = models.DateTimeField('Start Time')
    end = models.DateTimeField('End Time')
    duration = models.IntegerField('Duration in minutes', help_text="Duration in minutes")
    description = models.CharField(max_length=20, help_text="Individual Description (default = Description from WBS/PSP)")
    element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') # pylint: disable=maybe-no-member



# move to own app -> SAP


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
