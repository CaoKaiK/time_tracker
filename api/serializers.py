from rest_framework import serializers

from settings.models import Activity
from tracker.models import Customer, Group, Project

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = []

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [
            'project_name',
            'active',
        ]

