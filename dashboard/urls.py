from django.urls import path

from dashboard.views import groupView, flexView

urlpatterns = [
    path('', flexView, name='dash-flex'),
    path('group', groupView, name='dash-group')
]