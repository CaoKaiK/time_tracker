from django import forms
from django.db import models
from django.forms import ModelForm

from settings.models import Activity, Tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            'tag_name',
            'tag_hex'
        ]

