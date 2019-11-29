from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin


from .models import Project


def home(request):
    return render(request, 'tracker/home.html')

# class ProjectListView(ListView):
#     model = Project
        
# class ProjectDetailView(DetailView):
#     model = Project
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
#         context['elements'] = Element.objects.filter(project_id = self.object.id) # pylint: disable=maybe-no-member
#         return context

# class ProjectCreateView(SuccessMessageMixin, CreateView):
#     model = Project
#     fields = [
#         'project_name',
#         'country_name',
#         'customer_name',
#         'customer_street',
#         'customer_postal',
#         'customer_city',
#         ]
    
    
#     success_message = "Project %(project_name)s was created"
#     def get_success_url(self):
#         return reverse('projects-detail', kwargs={'pk': self.object.pk})

# class ProjectUpdateView(SuccessMessageMixin, UpdateView):
#     model = Project
#     fields = [
#         'project_name',
#         'country_name',
#         'customer_name',
#         'customer_street',
#         'customer_postal',
#         'customer_city',
#         'active',
#     ]
#     success_message = "Project %(project_name)s was updated"
#     def get_success_url(self):
#         return reverse('projects-detail', kwargs={'pk': self.object.pk})

# class ProjectDeleteView(DeleteView):
#     model = Project
#     success_url = reverse_lazy('projects-list')
#     success_message = "Project was deleted"

#     def delete(self, request, *args, **kwargs):
#         messages.warning(self.request, self.success_message)
#         return super(ProjectDeleteView, self).delete(request, *args, **kwargs)







# class ElementDetailView(DetailView):
#     model = Element

#     def get_context_data(self, *args, **kwargs):
#         context = super(ElementDetailView, self).get_context_data(*args, **kwargs)
#         context['entries'] = Entry.objects.filter(element_id = self.object.id) # pylint: disable=maybe-no-member
#         return context

# class ElementCreateView(SuccessMessageMixin, CreateView):
#     model = Element
#     fields = [
#         'element',
#         'act_description',
#         'act_type',
#         'act',
#     ]
    
#     def get_context_data(self, **kwargs):
#         context = super(ElementCreateView, self).get_context_data(**kwargs)
#         project = Project.objects.get(id=self.kwargs.get('pk')) # pylint: disable=maybe-no-member
#         context.update({'project': project})
#         return context

#     def form_valid(self, form):
#         form.instance.project_id = self.kwargs.get('pk')
#         return super(ElementCreateView, self).form_valid(form)

#     success_message = "Element %(element)s was created"
#     def get_success_url(self):
#         return reverse('projects-detail', kwargs={'pk': self.object.project_id})

# class ElementUpdateView(SuccessMessageMixin, UpdateView):
#     model = Element
#     fields = [
#         'project',
#         'element',
#         'act_description',
#         'act_type',
#         'act',
#         'active'
#     ]

#     success_message = "Element %(element)s was updated"
#     def get_success_url(self):
#         return reverse('projects-detail', kwargs={'pk': self.object.project.pk})

# class ElementDeleteView(DeleteView):
#     model = Element
#     #success_url = reverse_lazy('projects-detail')
#     success_message = "Element was deleted"

#     def delete(self, request, *args, **kwargs):
#         messages.warning(self.request, self.success_message)
#         return super(ElementDeleteView, self).delete(request, *args, **kwargs)

#     def get_success_url(self):
#         return reverse('projects-detail', kwargs={'pk': self.object.project_id})






# class EntryListView(ListView):
#     model = Entry

# class EntryDetailView(DetailView):
#     model = Entry

# class EntryCreateView(SuccessMessageMixin, CreateView):
#     model = Entry
#     fields = [
#         'element',
#         'date',
#         'duration',
#         'rest',
#         'description',
#         'booked',        
#     ]

    

# class EntryFromWBSCreateView(EntryCreateView):
#     fields = [
#         'date',
#         'duration',
#         'rest',
#         'description',
#         'booked',        
#     ]
    
#     def form_valid(self, form):
#         form.instance.element_id = self.kwargs.get('pk')
#         return super(EntryFromWBSCreateView, self).form_valid(form)
#     success_message = "Entry was created"

#     def get_success_url(self):
#         return reverse('projects-element-detail', kwargs={'pk_pro': self.object.element.project_id, 'pk': self.object.element_id})

# class EntryUpdateView(SuccessMessageMixin, UpdateView):
#     model = Entry
#     fields = [
#         'element',
#         'date',
#         'duration',
#         'rest',
#         'description',        
#         'booked',
#     ]

#     success_message = "Entry for %(element)s was updated " 
#     def get_success_url(self):
#         return reverse('entries-detail', kwargs={'pk': self.object.pk})

# class EntryDeleteView(DeleteView):
#     model = Entry

#     success_message = "Entry was deleted"

#     def delete(self, request, *args, **kwargs):
#         messages.warning(self.request, self.success_message)
#         return super(EntryDeleteView, self).delete(request, *args, **kwargs)

#     def get_success_url(self):
#         return reverse('projects-element-detail', kwargs={'pk_pro': self.object.element.project_id, 'pk': self.object.element_id})