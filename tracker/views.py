from django.shortcuts import render
from django.views.generic import ListView

from .models import Project, Entry


def home(request):
    return render(request, 'tracker/home.html')

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

class EntryListView(ListView):
    model = Entry