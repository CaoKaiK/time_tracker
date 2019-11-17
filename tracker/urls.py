from django.urls import path

from .views import (
    ProjectListView, 
    ProjectDetailView, 
    EntryListView)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('entries/', EntryListView.as_view(), name='entries'),
]