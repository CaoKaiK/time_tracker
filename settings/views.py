from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.db import transaction

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView, 
    DeleteView
)

from django.contrib.messages.views import SuccessMessageMixin

from settings.models import User, Contract, Activity, Tag
from settings.forms import TagForm


class ContractListView(ListView):
    model = Contract

    def get_context_data(self, *args, **kwargs):
        context = super(ContractListView, self).get_context_data(*args, **kwargs)
        context['user'] = User.objects.first() # pylint: disable=maybe-no-member
        return context


def settings(request):
    return render(request, 'settings/settings_base.html')

def manage_tags(request):
    TagModelFormSet = modelformset_factory(Tag, form=TagForm)

    template_name = 'settings/tag_form.html'

    if request.method == 'GET':
        formset = TagModelFormSet()
    
    elif request.method == 'POST':

        formset = TagModelFormSet(request.POST, request.FILES)

        
        if formset.is_valid():
            update_tags = []
            tag_id = 0
            
            for form in formset:
                tag_name = form.cleaned_data.get('tag_name')
                tag_hex = form.cleaned_data.get('tag_hex')

                if tag_hex and tag_hex:
                    update_tags.append(Tag(id=tag_id,tag_name=tag_name, tag_hex=tag_hex))
                    # keep primary keys static
                    tag_id +=1
                
            try:
                with transaction.atomic():
                    for tag in update_tags:
                        print(tag.tag_name)
                        existing_Tag = Tag.objects.filter(id=tag.id)
                        if existing_Tag:                        
                            existing_Tag.update(tag_name=tag.tag_name, tag_hex=tag.tag_hex)
                        else:
                            Tag.objects.create(id=tag.id, tag_name=tag.tag_name, tag_hex=tag.tag_hex)

                    messages.success(request, 'Tags were updated succesfully')
            except:
                    messages.warning(request, 'Some error occured. Tags were restored')

            return redirect('settings-tags')

    return render(request, template_name, {'formset': formset})

