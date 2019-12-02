from django.db import models
from django.core import validators


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
        return f'{self.activity_name}-{self.description}'

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