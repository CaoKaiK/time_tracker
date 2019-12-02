from django import forms
from django.db import models
from django.forms import ModelForm

from tracker.models import Customer, Group, Element

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        

