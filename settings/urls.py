from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.settings, name='settings-personal'),
    path('tags/', views.manage_tags, name='settings-tags')
]
