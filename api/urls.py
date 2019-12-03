from django.urls import include, path

from rest_framework import routers

from api.views import (
    ActivityViewSet,
    TagViewSet,
    CustomerViewSet,
    GroupViewSet,
    ElementViewSet
    )

router = routers.DefaultRouter()
router.register(r'activites', ActivityViewSet)
router.register(r'tags', TagViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'elements', ElementViewSet)


urlpatterns = [
    path('', include(router.urls), name='api-v1'),
]
