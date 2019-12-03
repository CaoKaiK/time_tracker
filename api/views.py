from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from settings.models import Activity, Tag
from tracker.models import Customer, Group, Element

from .serializers import (
    ActivitySerializer,
    TagSerializer,
    )



# API VIEWS
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ActivitySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all() # pylint: disable=maybe-no-member
    serializer_class = TagSerializer



