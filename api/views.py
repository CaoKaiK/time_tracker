from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from tracker.models import Project

from .serializers import ProjectSerializer



# API VIEWS



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ProjectSerializer

