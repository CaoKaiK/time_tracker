from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    EntryListView)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name="projects-create"),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='projects-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name="projects-delete"),
    path('entries/', EntryListView.as_view(), name='entries'),
]