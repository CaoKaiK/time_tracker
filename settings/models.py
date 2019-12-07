from django.db import models
from django.core import validators

import datetime


class User(models.Model):
    user_name = models.CharField(max_length=30,)
    user_img = models.ImageField(blank=True, null=True, upload_to='img/')
    location = models.CharField(max_length=30,)
    org_name = models.CharField(max_length=30,)
    ccenter = models.CharField(max_length=6,)
    start = models.DateField()

    def __str__(self):
        return self.user_name

    @property 
    def weekly_hours(self):
        current = Contract.objects.first()
        if current:
            return current.target*5
        else:
            return datetime.timedelta(0,0)

    
class Contract(models.Model):
    date = models.DateField(primary_key=True)
    target = models.DurationField(default=datetime.timedelta(hours=7))
    


    class Meta:
        ordering = ['-date']

    def __str__(self):
        h_day = int(self.target.total_seconds()/3600)
        return f'{str(self.date)} | {h_day} h'


class Activity(models.Model):
    '''
    Activity Model - Collection of Activities defined within the company
    Initialised entries: TG1, TG2, TG3, TG5, TG7
    '''
    activity_name = models.CharField(
        max_length=3,
        verbose_name='Activity: Activity Name',
        help_text='Activity (e.g. TG1, TG2, TG3, ...)'
        )
    description = models.CharField(
        max_length=20,
        verbose_name='Activity: Description',
        help_text='Activity description'
        )
    productive = models.BooleanField(
        default=False,
        verbose_name='Activity: Productive',
        help_text='Is this Activity considered to be productive'
        )

    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        ordering = ['activity_name']

    def __str__(self):
        return f'{self.activity_name} - {self.description}'

    def get_absolute_url(self):
        return None

class Tag(models.Model):
    '''
    Tag Model - Customizeable tags that can be attributed to elements or entries for evaluation and cosmetics
    Hex is used for HTML tags
    '''
    tag_name = models.CharField(
        max_length=20,
        verbose_name='Tag Name',
        help_text='Tag Name'
        )
    tag_hex = models.CharField(
        max_length=6, 
        validators=[
            validators.RegexValidator(regex='^([0-9a-fA-F]{6})$', message='No valid Hex Color code')
        ],
        verbose_name='Color:',
        help_text='Tag Color in Hexadecimal'
        )

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return f'{self.tag_name}'

    def get_absolute_url(self):
        return None

    @property
    def light_hex(self):
        return f'#{self.tag_hex}'

    @property
    def dark_hex(self):
        import matplotlib.colors as mc
        import colorsys
        amount = 0.8 #darken color
        c = f'#{self.tag_hex}'
        c = colorsys.rgb_to_hls(*mc.to_rgb(c))
        c_dark = colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])
        return c_dark