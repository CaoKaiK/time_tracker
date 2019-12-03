from rest_framework import serializers

from settings.models import Activity, Tag
from tracker.models import Customer, Group, Element

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


