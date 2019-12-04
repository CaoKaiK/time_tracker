from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls), 
    path('api/v1/', include('api.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('settings/', include('settings.urls')),   
    
    path('', include('tracker.urls')),
]
