from django.shortcuts import render
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response



from settings.models import Activity, Tag
from tracker.models import Customer, Group, Element, Entry, Day

from .serializers import (
    ActivitySerializer,
    TagSerializer,
    CustomerSerializer,
    GroupSerializer,
    ElementSerializer,
    DaySerializer,
    EntrySerializer
    )


# general API views
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ActivitySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all() # pylint: disable=maybe-no-member
    serializer_class = TagSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all() # pylint: disable=maybe-no-member
    serializer_class = CustomerSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all() # pylint: disable=maybe-no-member
    serializer_class = GroupSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ElementSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all() # pylint: disable=maybe-no-member
    serializer_class = DaySerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all() # pylint: disable=maybe-no-member
    serializer_class = EntrySerializer

# chart endpoints

DEFAULT_COLORS = [
    'rgba(0, 100, 110, 0.5)',
    'rgba(180, 75, 40, 0.5)',
    'rgba(85, 110, 40, 0.5)',
    'rgba(100, 25, 70, 0.5)',
    'rgba(35, 145, 150, 0.5)',
    'rgba(235, 120, 10, 0.5)',
    'rgba(135, 150, 40, 0.5)',
    'rgba(155, 30, 80, 0.5)',
    'rgba(75, 185, 185, 0.5)',
    'rgba(255, 185, 0, 0.5)',
    'rgba(190, 195, 40, 0.5)',
    'rgba(215, 105, 140, 0.5)'
]

DEFAULT_BORDERS = [
    'rgba(0, 100, 110, 1)',
    'rgba(180, 75, 40, 1)',
    'rgba(85, 110, 40, 1)',
    'rgba(100, 25, 70, 1)',
    'rgba(35, 145, 150, 1)',
    'rgba(235, 120, 10, 1)',
    'rgba(135, 150, 40, 1)',
    'rgba(155, 30, 80, 1)',
    'rgba(75, 185, 185, 1)',
    'rgba(255, 185, 0, 1)',
    'rgba(190, 195, 40, 1)',
    'rgba(215, 105, 140, 1)'
]

class GroupSum(APIView):
    """
    Group Sum View

    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        group_names = []
        group_hours = []
        background_colors = []
        border_colors = []
        i = 0
        for group in Group.objects.all():
            
            entries = Entry.objects.filter(element__group = group.id)
            if entries:
                hours_sum = entries.aggregate(Sum('duration'))['duration__sum'].total_seconds()/3600
                group_names.append(group.group_name)
                group_hours.append(hours_sum)
                background_colors.append(DEFAULT_COLORS[i])
                border_colors.append(DEFAULT_BORDERS[i])
                i += 1

        data = {
            'names': group_names,
            'hours': group_hours,
            'background': background_colors,
            'border': border_colors
        }
    
        return Response(data)

        

class TestGroupData(APIView):
    """
    Test View

    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        group_names = [group.group_name for group in Group.objects.all()]
        return Response(group_names)