from django.db import models

from datetime import datetime, timedelta


class Project(models.Model):
    project_name = models.CharField(max_length=20, help_text='Internal Project Name')
    country_name = models.CharField(max_length=30, help_text='Country of Customer/Project')
    customer_name = models.CharField(max_length=30, blank=True, null=True, help_text='Customer Name')
    customer_street = models.CharField(max_length=50, blank=True, null=True, help_text='Customer Address Street')
    customer_postal = models.CharField(max_length=15, blank=True, null=True, help_text='Customer Postal Code')
    customer_city = models.CharField(max_length=30, blank=True, null=True, help_text='Customer City')

    active = models.BooleanField(default=True, help_text='Project is still active')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_subfeature_elements(self):
        return self.element_set.filter(project_id = self.id) # pylint: disable=maybe-no-member

    def __str__(self):
        return self.project_name

class Element(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    element = models.CharField(max_length=24, help_text='WBS/PSP-Element')
    act_description = models.CharField(max_length=20, help_text='Describes the general activity for this WBS/PSP')
    act_type = models.CharField('Activity Type', max_length=6, help_text='Activity Type for this WBS/PSP')
    act = models.IntegerField('Activity', help_text='Activity for this WBS/PSP')

    active = models.BooleanField(default=True, help_text='WBS is still active')
    
    def get_subfeature_entries(self):
        return self.entry_set.filter(element_id = self.id) # pylint: disable=maybe-no-member

    def __str__(self):
        return self.element


class Entry(models.Model):
    element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True, default=None)
    date = models.DateField('Date', default=datetime.now)
    duration = models.IntegerField('Duration', help_text='Duration in minutes')
    rest = models.IntegerField('Resting Period', default=0, help_text='Resting Period in minutes')    
    description = models.CharField(max_length=20, help_text='Individual Description (default = Description from WBS/PSP)')
    booked = models.BooleanField('Booked', default=False, help_text='Entry is booked in SAP')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') # pylint: disable=maybe-no-member



# move to own app -> SAP


