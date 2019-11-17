from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Project, Entry


def home(request):
    return render(request, 'tracker/home.html')

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 10

class ProjectDetailView(DetailView):
    model = Project

class EntryListView(ListView):
    model = Entry