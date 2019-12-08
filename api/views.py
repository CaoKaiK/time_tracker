from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

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


# API VIEWS
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