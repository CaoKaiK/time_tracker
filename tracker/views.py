from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin


from .models import Project, Element, Entry


def home(request):
    return render(request, 'tracker/home.html')

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

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

class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    fields = [
        'project_name',
        'country_name',
    ]
    success_message = "Project %(project_name)s was updated"
    def get_success_url(self):
        return reverse('projects-detail', kwargs={'pk': self.object.pk})

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects-list')
    success_message = "Project was deleted"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)

class ElementCreateView(CreateView):
    model = Element
    fields = [
        'element',
        'act_description',
        'act_type',
        'act',
    ]

    def form_valid(self, form):
        form.instance.project_id_id = self.kwargs.get('pk')
        return super(ElementCreateView, self).form_valid(form)



class EntryListView(ListView):
    model = Entry