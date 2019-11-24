from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ElementDetailView,
    ElementCreateView,
    ElementUpdateView,
    ElementDeleteView,
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    )
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name="projects-create"),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='projects-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name="projects-delete"),
    path('projects/<int:pk_pro>/element/<int:pk>', ElementDetailView.as_view(), name='projects-element-detail'),
    path('projects/<int:pk>/element/create', ElementCreateView.as_view(), name='projects-element-create'),
    path('projects/<int:pk_pro>/element/<int:pk>/update', ElementUpdateView.as_view(), name='projects-element-update'),
    path('projects/<int:pk_pro>/element/<int:pk>/delete', ElementDeleteView.as_view(), name='projects-element-delete'),
    path('entries/', EntryListView.as_view(), name='entries'),
    path('entries/<int:pk>', EntryDetailView.as_view(), name='entries-detail'),
    path('entries/<int:pk>/update', EntryUpdateView.as_view(), name='entries-update'),


]