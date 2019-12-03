from django.db import models
from django.urls import reverse

from datetime import datetime, timedelta

from settings.models import Activity, Tag


class Customer(models.Model):
    '''
    Customer Model - can be attributed to Group
    '''
    customer_name = models.CharField(
        max_length = 50,
        verbose_name = 'Customer Name',
        help_text = 'Customer Name'
        )
    country = models.CharField(
        max_length = 50,
        verbose_name = 'Country',
        help_text = 'Customer Country'
        )
    city = models.CharField(
        max_length = 50,
        blank = True,
        verbose_name = 'City',
        help_text = 'Customer City'
        )
    street = models.CharField(
        max_length = 50,
        blank = True,
        verbose_name = 'Street',
        help_text = 'Customer Street'
        )
    postal = models.CharField(
        max_length = 20,
        blank = True,
        verbose_name = 'Postal',
        help_text = 'Customer Postal Code'
        )

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('group-list')

class Group(models.Model):
    '''
    Group Model - groups elements into Element Groups
    '''
    # rows for order in Group List
    ROW1 = 1
    ROW2 = 2
    ROW3 = 3
    ROW_CHOICES = [
        (ROW1, 'Row 1'),
        (ROW2, 'Row 2'),
        (ROW2, 'Row 3',)
    ]

    group_name = models.CharField(
        max_length = 20,
        verbose_name = 'Group Name',
        help_text = 'Element Group Name'
        )
    # FK to customer: zero or one to many or none
    customer = models.ForeignKey(
        Customer,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        default = None,
        verbose_name = 'Customer Name',
        related_name = 'groups',
        help_text = 'Customer'
        )
    active = models.BooleanField(
        default = True, 
        verbose_name = 'Active',
        help_text = 'Is this Element Group still active?'
        )
    row = models.IntegerField(choices=ROW_CHOICES, default=ROW1)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse('group-list')
    

class Element(models.Model):
    '''
    Element Model - Each element represents a separate cost entity. Due to the different combination of booking
    certain atrributes of the entity can be left blank.

    *Leistungs Art : Activity Type (includes hourly rate)
    *Taetigkeit : Activity
    *Empfaenger Stelle : Receiver Cost Center
    *PSP : WBS
    *Empfaenger Auftrag : Receiver Order

    Activity (TG1, TG2, ...) and hourly rate (021, F21, S21) can be combined to receive the activity type. 
    Vice versa if the Activity Type is available the Activity and hourly rate can be derived.

    Project Work generally addresses cost via a WBS the Activity and the Activity Type

    Holiday, Sickleave addresses cost via Cost Center and Activity
    '''
    # FK to group: zero or one to many or none
    group = models.ForeignKey(
        Group,
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        related_name = 'elements'
        )
    # FK to tag: tero or one to many or none
    activity = models.ForeignKey(
        Activity,
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        related_name = 'elements'
        )

    code_act_type = models.CharField(
        max_length = 3,
        blank = True,
        verbose_name = 'Activity Type Code',
        help_text = 'Code to identify hourly rate (e.g. 012 in TG1012)',
        )
    receiver_ccenter = models.CharField(
        max_length = 5,
        blank = True,
        default = None,
        verbose_name = 'Receiver Cost Center'
        )
    wbs_element = models.CharField(
        max_length = 20,
        blank = True,
        default = None,
        verbose_name = 'WBS Element Name'
        )
    receiver_order = models.CharField(
        max_length = 6,
        blank = True,
        default = None,
        verbose_name = 'Receiver Order'
        )
    description = models.CharField(max_length=20, verbose_name='Description')
    tag = models.ForeignKey(
        Tag,
         on_delete = models.SET_NULL,
         blank = True,
         null = True,
         default = None,
         related_name = 'elements'
         )
    active = models.BooleanField(
        default = True, 
        verbose_name = 'Active',
        help_text = 'Is this Element still active?'
        )

    class Meta:
        verbose_name = 'element'
        verbose_name_plural = 'elements'
    
    def __str__(self):
        return f'{self.receiver_ccenter} | {self.wbs_element} | {self.description}'

    def get_absolute_url(self):
        return None

    @property
    def activity_type(self):
        if self.code_act_type:
            return f'{self.activity.activity_name}{self.code_act_type}' # pylint: disable=maybe-no-member
        else:
            return ''
    @property
    def project_or_group_name(self):
        if self.group is not None:
            return self.group.group_name # pylint: disable=maybe-no-member
        else:
            return None

class Entry(models.Model):
    element = models.ForeignKey(
        Element,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        default = None,
        related_name = 'entries'
        )
    # reference Day model as string as day has not been defined yet
    date = models.ForeignKey(
        'Day',
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        related_name = 'entries'
    )
    start = models.TimeField(verbose_name='Starting Time')
    end = models.TimeField(verbose_name='Ending Time')
    timeout = models.DurationField(verbose_name='Duration of break time')
    duration = models.DurationField(verbose_name='Duration of time attributed to Element')
    description = models.CharField(max_length=20, verbose_name='Description of Entry (default is description of parent Element)')
    tag = models.ForeignKey(
        Tag,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        default = None,
        related_name = 'entries'
    )

    class Meta:
        ordering = ['-date']
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return f'{str(self.date)} {self.element} {self.id}'

    def get_absolute_url(self):
        return None
    

class Day(models.Model):
    date = models.DateField(primary_key=True)
    element = models.ManyToManyField('Element', through=Entry, related_name='days')

    def __str__(self):
        return str(self.date)