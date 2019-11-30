from rest_framework import serializers

from settings.models import Activity, Tag
from tracker.models import Customer, Group, Project

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id',
            'activity_name',
            'description',
            'productive'
        ]

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'tag_name',
            'tag_hex',
        ]

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [
            'project_name',
            'active',
        ]

