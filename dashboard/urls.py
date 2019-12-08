from django.urls import path

from . import views

urlpatterns = [
    path('', views.testView, name='dash-flex'),
    path('group', views.testView, name='dash-group')
    
]