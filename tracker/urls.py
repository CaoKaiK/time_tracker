from django.urls import path, include

from .views import (
    GroupListView,
    GroupDetailView,
    GroupCreateView,
    GroupUpdateView,
    GroupDeleteView,
    ElementDetailView,
    ElementCreateView,
    ElementUpdateView,
    ElementDeleteView,
    DayDetailView,

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
            path('create/', ElementCreateView.as_view(), name='group-element-create'),
            path('<int:pk>', include([
                path('', ElementDetailView.as_view(), name='group-element-detail'),
                path('update/', ElementUpdateView.as_view(), name='group-element-update'),
                path('delete/', ElementDeleteView.as_view(), name='group-element-delete'),

            ])),
             
        ])),
    ])),
    path('entry/', include([
        path('day/', include([
            path('<pk>/', DayDetailView.as_view(), name='day-detail')
        ]))
    ])),

    #path('projects/', ProjectListView.as_view(), name='projects-list'),
    #path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    #path('projects/create/', ProjectCreateView.as_view(), name="projects-create"),
    #path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='projects-update'),
    #path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name="projects-delete"),
    # path('projects/<int:pk_pro>/element/<int:pk>', ElementDetailView.as_view(), name='projects-element-detail'),
    # path('projects/<int:pk>/element/create', ElementCreateView.as_view(), name='projects-element-create'),
    # path('projects/<int:pk_pro>/element/<int:pk>/update', ElementUpdateView.as_view(), name='projects-element-update'),
    # path('projects/<int:pk_pro>/element/<int:pk>/delete', ElementDeleteView.as_view(), name='projects-element-delete'),
    # path('projects/<int:pk_pro>/element/<int:pk>/entry/create', EntryFromWBSCreateView.as_view(), name='projects-element-entry-create'),
    # path('entries/', EntryListView.as_view(), name='entries'),
    # path('entries/<int:pk>', EntryDetailView.as_view(), name='entries-detail'),
    # path('entries/create', EntryCreateView.as_view(), name='entries-create'),
    # path('entries/<int:pk>/update', EntryUpdateView.as_view(), name='entries-update'),
    # path('entries/<int:pk>/delete', EntryDeleteView.as_view(), name='entries-delete'),
]