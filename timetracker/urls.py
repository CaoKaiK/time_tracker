from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from . import settings
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls), 
    path('api/v1/', include('api.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('settings/', include('settings.urls')),   
    
    path('', include('tracker.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)