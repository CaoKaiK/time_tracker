from django.db import models

class Activity(models.Model):
    '''
    Activity Model - Collection of Activities defined within the company
    Initialised entries: TG1, TG2, TG3, TG5, TG7
    '''
    activity_name = models.CharField(max_length=3, help_text='Activity (e.g. TG1, TG2, TG3, ...)')
    description = models.CharField(max_length=20, help_text='Activity description')
    productive = models.BooleanField(default=False, help_text='Is this Activity considered to be productive')

    def __str__(self):
        return f'{self.activity_name}-{self.description}'



class Tag(models.Model):
    '''
    Tag Model - Customizeable tags that can be attributed to elements or entries for evaluation and cosmetics
    Hex is used for HTML tags
    '''
    tag_name = models.CharField(max_length=20, help_text='Tag Name')
    tag_hex = models.CharField(max_length=6, help_text='Tag Color in Hex')