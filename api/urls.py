from django.urls import include, path

from rest_framework import routers

from .views import (
    ActivityViewSet,
    TagViewSet,
    )

router = routers.DefaultRouter()
router.register(r'activites', ActivityViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = [
    path('', include(router.urls), name='api-v1'),
]
