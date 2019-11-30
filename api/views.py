from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from settings.models import Activity, Tag
from tracker.models import Project

from .serializers import (
    ActivitySerializer,
    TagSerializer,
    ProjectSerializer
    )



# API VIEWS
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ActivitySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all() # pylint: disable=maybe-no-member
    serializer_class = TagSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ProjectSerializer

