from django.urls import path

from .views import ProjectListView, EntryListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', ProjectListView.as_view(), name='projects'),
    path('entries', EntryListView.as_view(), name='entries'),
]