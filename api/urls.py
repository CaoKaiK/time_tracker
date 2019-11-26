from django.urls import include, path

from rest_framework import routers

from .views import ProjectViewSet, ElementViewSet, EntryViewSet
from .views import ListProjects

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'entry', EntryViewSet)

urlpatterns = [
    path('', include(router.urls), name='api-v1'),
    path('data2', ListProjects.as_view()),
]
