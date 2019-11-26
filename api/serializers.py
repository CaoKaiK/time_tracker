from rest_framework import serializers

from tracker.models import Project, Element, Entry

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [
            'project_name',
            'country_name',
            'customer_name',
            'customer_street',
            'customer_postal',
            'customer_city',
            'active',
            'created_date',
            'modified_date',
        ]

class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = [
            'project',
            'element',
            'act_description',
            'act_type',
            'act',
            'active'
        ]

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = [
            'element',
            'date',
            'duration',
            'rest',
            'description',
            'booked',
        ]