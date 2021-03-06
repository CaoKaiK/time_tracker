from django.db import models
from django.urls import reverse
from django.db.models import Sum

import datetime

from settings.models import User, Contract, Activity, Tag


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
        (ROW3, 'Row 3',)
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
        on_delete = models.CASCADE,
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
        if self.wbs_element:
            return f'{self.wbs_element} | {self.description}'
        elif self.receiver_ccenter:
            if self.receiver_order:
                return f'{self.receiver_ccenter} | {self.receiver_order} | {self.description}'
            else:
                return f'{self.receiver_ccenter} | {self.description}'
        else:
            return f'{self.description}'
        

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
        on_delete = models.CASCADE,
        related_name = 'entries'
        )
    # reference Day model as string as day has not been defined yet
    date = models.ForeignKey(
        'Day',
        on_delete = models.CASCADE,
        related_name = 'entries'
    )
    
    duration = models.DurationField(verbose_name='Duration of time attributed to Element', help_text='Duration in HH:mm:ss Format')
    description = models.CharField(
        max_length = 20,
        blank = True,
        verbose_name = 'Description of Entry',
        help_text = 'Will inherit description from Element if left empty'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        default = None,
        related_name = 'entries',
        help_text='Will inherit Tag from Element if left empty and Element has a Tag'
    )

    class Meta:
        ordering = ['-date']
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return f'{str(self.date)} {self.element} {self.id}' # pylint: disable=maybe-no-member

    def get_absolute_url(self):
        return None
    
    @property
    def start(self):
        query = self.date.entries.first()
        if query:
            return query.end
        else:
            return self.date.start
    
    @property
    def end(self):
        return self.start + self.duration
  
class Day(models.Model):
    date = models.DateField(primary_key=True)
    element = models.ManyToManyField('Element', through=Entry, related_name='days')
    start = models.TimeField(default=datetime.time(9,0) ,verbose_name='Working Day Start Time',)
    end = models.TimeField(default=datetime.time(9,0), verbose_name='Working Day End Time')
    timeout = models.DurationField(default=datetime.timedelta(0), verbose_name='Total Break on this day')
    withdrawal = models.DurationField(default=datetime.timedelta(0), verbose_name='One-time withdrawal')


    is_vacation = models.BooleanField(verbose_name='Vacation', default=False)
    is_public_holiday = models.BooleanField(verbose_name='Public Holiday', default=False)

    def __str__(self):
        return str(self.date)

    @property
    def is_weekend(self):
        '''0,1,2,3,4 = Mon, Tue, Wed, Thu, Fri'''
        if self.date.weekday() > 4:
            return True
        else:
            return False

    @property
    def total_duration(self):
        start = datetime.datetime.combine(datetime.date.today(), self.start)
        end = datetime.datetime.combine(datetime.date.today(), self.end)
        return end - start - self.timeout

    @property
    def entries_sum_duration(self):
        query = self.entries.aggregate(Sum('duration'))['duration__sum']
        if query:
            return query
        else:
            return datetime.timedelta(0,0)

    @property
    def target(self):
        if self.is_public_holiday or self.is_weekend:
            return datetime.timedelta(0,0)
        else:
            query = Contract.objects.filter(date__lte=self.date).first()
            if query:
                return query.target
            else:
                return datetime.timedelta(hours=7)

    @property
    def balance_day(self):
        balance = self.entries_sum_duration - self.target - self.withdrawal
        return balance
    
