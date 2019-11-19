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


        
class ProjectDetailView(DetailView):
    model = Project
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        context['elements'] = Element.objects.filter(project_id = self.object.id) # pylint: disable=maybe-no-member
        return context

class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    fields = [
        'project_name',
        'country_name',
        'customer_name',
        'customer_street',
        'customer_postal',
        ]
    success_message = "Project %(project_name)s was created"
    def get_success_url(self):
        return reverse('projects-detail', kwargs={'pk': self.object.pk})

class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    fields = [
        'project_name',
        'country_name',
        'customer_name',
        'customer_street',
        'customer_postal',
        'active',
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

class ElementCreateView(SuccessMessageMixin, CreateView):
    model = Element
    fields = [
        'element',
        'act_description',
        'act_type',
        'act',
    ]
    def form_valid(self, form):
        form.instance.project_id = self.kwargs.get('pk')
        return super(ElementCreateView, self).form_valid(form)

    success_message = "Element %(element)s was created"
    def get_success_url(self):
        return reverse('projects-detail', kwargs={'pk': self.object.project_id})




class EntryListView(ListView):
    model = Entry