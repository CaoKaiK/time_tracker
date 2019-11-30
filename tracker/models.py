from django.db import models

from datetime import datetime, timedelta

from settings.models import Activity, Tag


class Customer(models.Model):
    '''
    Customer Model - can be attributed to Group or Project
    '''
    customer_name = models.CharField(
        max_length=50,
        verbose_name='Customer: Customer Name',
        help_text='Customer Name'
        )
    country = models.CharField(
        max_length=50,
        verbose_name='Customer: Country',
        help_text='Customer Country'
        )
    city = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Customer: City',
        help_text='Customer City'
        )
    street = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Customer: Street',
        help_text='Customer Street'
        )
    postal = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Customer: Postal',
        help_text='Customer Postal Code'
        )

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return None

class Group(models.Model):
    '''
    Group Model - for activity types that don't fall under project-related work.
    No WBS available or combination of receiver cost center, receiver order
    Examples: TG3, TG4, TG5, TG7 ...
    '''
    group_name = models.CharField(
        max_length=20,
        verbose_name='Group: Group Name',
        help_text='Activity Group Name'
        )
    # FK to customer: zero or one to many or none
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='groups'
        )
    active = models.BooleanField(
        default=True, 
        verbose_name='Group: Active',
        help_text='Is this Activity Group still active?'
        )

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return None

class Project(models.Model):
    '''
    Project Model - for activity that can be linked to a Project.
    Requires a WBS Element and activity type (e.g. TG1021)
    Examples: Project XY - Unit 1
    '''
    project_name = models.CharField(
        max_length=20,
        verbose_name='Project: Project Name',
        help_text='Project Name'
        )
    # FK to customer: zero or one to many or none
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='projects'
        )
    active = models.BooleanField(
        default=True,
        verbose_name='Project: Active',
        help_text='Is this Project still active?'
        )
    
    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return None


class Element(models.Model):
    '''
    Element Model - Each element represents a separate cost entity. Due to the different combination of 
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
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='elements'
        )
    # FK to project: zero or one to many or none
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='elements'
        )
    # FK to tag: one and only one to many or none, CASCADE DELETE!!!
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='elements'
        )

    code_act_type = models.CharField(
        max_length=3,
        blank=True,
        verbose_name='Element: Activity Type Code',
        help_text='Code to identify hourly rate (e.g. 012 in TG1012)',
        )
    receiver_ccenter = models.CharField(
        max_length=5,
        blank=True,
        default=None,
        verbose_name='Element: Receiver Cost Center'
        )
    wbs_element = models.CharField(
        max_length=20,
        blank=True,
        default=None,
        verbose_name='Element: WBS Element Name'
        )
    receiver_order = models.IntegerField(null=True, verbose_name='Elements: Receiver Order')
    description = models.CharField(max_length=20, verbose_name='Elements: Description')
    tag = models.ForeignKey(
        Tag,
         on_delete=models.SET_NULL,
         null=True,
         default=None,
         related_name='elements'
         )

    class Meta:
        verbose_name = 'element'
        verbose_name_plural = 'elements'
    
    def __str__(self):
        return f'{self.receiver_ccenter}{self.wbs_element}'

    def get_absolute_url(self):
        return None

    @property
    def activity_type(self):
        if self.code_act_type:
            return f'{self.activity.activity_name}{self.code_act_type}' # pylint: disable=maybe-no-member
        else:
            return None
    @property
    def project_or_group_name(self):
        if self.project is not None:
            return self.project.project_name # pylint: disable=maybe-no-member
        elif self.group is not None:
            return self.group.group_name # pylint: disable=maybe-no-member
        else:
            return None

