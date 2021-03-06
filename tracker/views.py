from datetime import datetime
import calendar

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.safestring import mark_safe

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView, 
    DeleteView
)

from django.contrib.messages.views import SuccessMessageMixin

from tracker.models import Customer, Group, Element, Entry, Day
from tracker.utils import Calendar, get_date, next_month, prev_month
from settings.models import Tag


def home(request):
    return render(request, 'tracker/home.html')


class CalendarView(ListView):
    model = Entry
    template_name = 'tracker/calendar_month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get today's day or process navigation
        d = get_date(self.request.GET.get('month', None))

        # Instantiate calendar
        cal = Calendar(d.year, d.month)

        # Process html template
        html_cal = cal.formatmonthview(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context






class GroupListView(ListView):
    model = Group
    ordering = ['-modified_date']

class GroupDetailView(DetailView):
    model = Group    

class GroupCreateView(SuccessMessageMixin, CreateView):
    model = Group
    fields = '__all__'
    success_message = 'Group %(group_name)s was created'

    def get_success_url(self):
        return reverse('group-list')

class GroupUpdateView(SuccessMessageMixin, UpdateView):
    model = Group
    fields = '__all__'
    success_message = 'Group %(group_name)s was updated'

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.id})

class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('group-list')
    success_message = 'Group was deleted'
    
    def get_context_data(self, *args, **kwargs):
        context = super(GroupDeleteView, self).get_context_data(*args, **kwargs)
        context['entries'] = Entry.objects.filter(element__group = self.object.id) # pylint: disable=maybe-no-member
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(GroupDeleteView, self).delete(request, *args, **kwargs)




class ElementDetailView(DetailView):
    model = Element

class ElementCreateFromListView(SuccessMessageMixin, CreateView):
    model = Element
    fields = [
        'activity',
        'code_act_type',
        'receiver_ccenter',
        'wbs_element',
        'receiver_order',
        'description',
        'tag'
    ]
    success_message = 'Element was created'

    def form_valid(self, form):
        group = Group.objects.get(id=self.kwargs.get('pk_group'))
        form.instance.group = group
        return super(ElementCreateFromListView, self).form_valid(form)

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.group.id})



class ElementUpdateView(SuccessMessageMixin, UpdateView):
    model = Element
    fields = '__all__'
    success_message = 'Element was updated'

    def get_success_url(self):
        return reverse('group-element-detail', kwargs={'pk_group': self.object.group.id, 'pk': self.object.id})    

class ElementDeleteView(DeleteView):
    model = Element
    #success_url = reverse_lazy('projects-detail')
    success_message = "Element was deleted"
    
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(ElementDeleteView, self).delete(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.group.id})





class DayDetailView(DetailView):
    model = Day

class DayUpdateView(SuccessMessageMixin, UpdateView):
    model = Day
    fields = [
        'start',
        'end',
        'timeout',
        'is_vacation',
        'is_public_holiday',
    ]

    success_message = "Day was updated"

    def get_success_url(self):
        print(self.object)
        return reverse('entry-day-update', kwargs={'pk': self.object.date})

class EntryCreateFromDayView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = [
        'element',
        'duration',
        'description',
        'tag'
    ]


    def form_valid(self, form):
        date = Day.objects.get(date=self.request.GET.get('date'))
        form.instance.date = date
        #inherit tag from element if empty and tag exists
        if not form.instance.tag and form.instance.element.tag_id:
            form.instance.tag = Tag.objects.get(id=form.instance.element.tag_id)
        
        if not form.instance.description:
            form.instance.description = Element.objects.get(id=form.instance.element_id).description

        return super(EntryCreateFromDayView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('entry-day-update', kwargs={'pk': self.object.date})


class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = '__all__'

    def get_success_url(self):
        return reverse('entry-day-update', kwargs={'pk': self.object.date})

class EntryDeleteView(SuccessMessageMixin, DeleteView):
    model = Entry

    success_message = "Entry was deleted"
    
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(EntryDeleteView, self).delete(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('entry-day-update', kwargs={'pk': self.object.date})

        
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