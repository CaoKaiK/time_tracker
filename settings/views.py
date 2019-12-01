from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.db import transaction

from settings.models import Activity, Tag
from settings.forms import TagForm

# Create your views here.

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
                print(form)
                tag_name = form.cleaned_data.get('tag_name')
                tag_hex = form.cleaned_data.get('tag_hex')

                if tag_hex and tag_hex:
                    update_tags.append(Tag(id=tag_id,tag_name=tag_name, tag_hex=tag_hex))
                    # keep primary keys static
                    tag_id +=1

            try:
                with transaction.atomic():
                    Tag.objects.all().delete()
                    Tag.objects.bulk_create(update_tags)

                    messages.success(request, 'Tags were updated succesfully')
            except:
                    messages.warning(request, 'Some error occured. Tags were restored')

            return redirect('settings-tags')

    return render(request, template_name, {'formset': formset})

