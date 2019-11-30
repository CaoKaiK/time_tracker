from django import forms
from django.db import models
from django.forms import ModelForm

from django.utils.translation import gettext_lazy as _

from settings.models import Activity, Tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

