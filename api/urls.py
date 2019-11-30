from django.urls import include, path

from rest_framework import routers

from .views import (
    ActivityViewSet,
    TagViewSet,
    ProjectViewSet
    )

router = routers.DefaultRouter()
router.register(r'activites', ActivityViewSet)
router.register(r'tags', TagViewSet)
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    path('', include(router.urls), name='api-v1'),
]
