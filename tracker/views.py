from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin

from .models import Project, Entry


def home(request):
    return render(request, 'tracker/home.html')

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 20

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    fields = [
        'project_name',
        'country_name',
        ]

    success_message = "Project %(project_name)s was created"

    def get_success_url(self):
        return reverse('projects-detail', kwargs={'pk': self.object.pk})

class EntryListView(ListView):
    model = Entry