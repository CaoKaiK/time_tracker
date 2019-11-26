from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from tracker.models import Project, Element, Entry

from .serializers import ProjectSerializer, ElementSerializer, EntrySerializer



# API VIEWS

class ListProjects(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        project_names = [project.project_name for project in Project.objects.all()] # pylint: disable=maybe-no-member
        return Response(project_names)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ProjectSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all() # pylint: disable=maybe-no-member
    serializer_class = ElementSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all() # pylint: disable=maybe-no-member
    serializer_class = EntrySerializer