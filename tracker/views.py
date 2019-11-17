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

class ProjectCreateView(CreateView, SuccessMessageMixin):
    model = Project
    fields = ['project_name']
    success_message = "Project %(name)s was created" #TO DO

    def get_success_url(self):
        return reverse('projects-detail', kwargs={'pk': self.object.pk})

class EntryListView(ListView):
    model = Entry