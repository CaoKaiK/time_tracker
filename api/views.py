from django.shortcuts import render
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response



from settings.models import Activity, Tag
from tracker.models import Customer, Group, Element, Entry, Day
from tracker.utils import get_date


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
    'rgba(0, 100, 110, 0.7)',
    'rgba(180, 75, 40, 0.7)',
    'rgba(85, 110, 40, 0.7)',
    'rgba(100, 25, 70, 0.7)',
    'rgba(35, 145, 150, 0.7)',
    'rgba(235, 120, 10, 0.7)',
    'rgba(135, 150, 40, 0.7)',
    'rgba(155, 30, 80, 0.7)',
    'rgba(75, 185, 185, 0.7)',
    'rgba(255, 185, 0, 0.7)',
    'rgba(190, 195, 40, 0.7)',
    'rgba(215, 105, 140, 0.7)'
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
    Sum of entries for all groups
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

class MonthHours(APIView):
    """
    Target and Reached Hours per Month
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        requested_date = get_date(request.GET.get('month', None))

        day_label = []
        hours_target = []
        hours_total = []
        i = 0

        for day in Day.objects.filter(date__year=requested_date.year).filter(date__month=requested_date.month):
            day_label.append(day.date)
            entries = day.entries.all()
            if entries:
                hours_sum = entries.aggregate(Sum('duration'))['duration__sum'].total_seconds()/3600
            else:
                hours_sum = 0
            day_target = day.target.total_seconds()/3600

            if i==0:
                hours_target.append(day_target)
                hours_total.append(hours_sum)
            else:
                hours_target.append(day_target + hours_target[i-1])
                hours_total.append(hours_sum + hours_total[i-1])
            i +=1

            month = hours_total[-1] - hours_target[-1]
        data = {
            'date': day_label,
            'target': hours_target,
            'total': hours_total,
            'month': month
        }

        return Response(data)

class TotalHours(APIView):
    """
    Flextime Account - Total Hours until today
    """
    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        return Response(None)



class TestGroupData(APIView):
    """
    Test View

    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        group_names = [group.group_name for group in Group.objects.all()]
        return Response(group_names)