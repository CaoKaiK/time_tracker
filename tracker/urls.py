from django.urls import path, include

from .views import (
    GroupListView,
    GroupDetailView,
    GroupCreateView,
    GroupUpdateView,
    GroupDeleteView,
    ElementDetailView,
    ElementCreateFromListView,
    ElementUpdateView,
    ElementDeleteView,
    DayUpdateView,
    EntryCreateFromDayView,
    EntryUpdateView,
    EntryDeleteView,
    CalendarView,
    
    )
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/', include([
        path('', GroupListView.as_view(), name='group-list'),
        path('create/', GroupCreateView.as_view(), name='group-create'),
        path('<int:pk>/', include([
            path('', GroupDetailView.as_view(), name='group-detail'),
            path('update/', GroupUpdateView.as_view(), name='group-update'),
            path('delete/', GroupDeleteView.as_view(), name='group-delete'),
        ])),
        path('<int:pk_group>/element/', include([            
            path('create/', ElementCreateFromListView.as_view(), name='group-element-create'),
            path('<int:pk>/', include([
                path('', ElementDetailView.as_view(), name='group-element-detail'),
                path('update/', ElementUpdateView.as_view(), name='group-element-update'),
                path('delete/', ElementDeleteView.as_view(), name='group-element-delete'),

            ])),
             
        ])),
    ])),
    path('entry/', include([
        path('create/', EntryCreateFromDayView.as_view(), name='entry-create-day'),
        path('<int:pk>/', include([
            path('', EntryUpdateView.as_view(), name='entry-update'),
            path('delete/', EntryDeleteView.as_view(), name='entry-delete'),
        ])),
        
        path('filter/day/<pk>/', CalendarView.as_view(), name='entry-filter-day'),
        path('month/', CalendarView.as_view(), name='entry-month'),
        path('day/', include([
            path('<pk>/', include([                
                path('', DayUpdateView.as_view(), name='entry-day-update'),                
                
            ])),
            
        ])),
    ])),
]