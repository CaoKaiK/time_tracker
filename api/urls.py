from django.urls import include, path

from rest_framework import routers

from api.views import (
    ActivityViewSet,
    TagViewSet,
    CustomerViewSet,
    GroupViewSet,
    ElementViewSet,
    EntryViewSet,
    DayViewSet,
    )

router = routers.DefaultRouter()
router.register(r'activites', ActivityViewSet)
router.register(r'tags', TagViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'group', GroupViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'days', DayViewSet)
router.register(r'entries', EntryViewSet)


urlpatterns = [
    path('', include(router.urls), name='api-v1'),
]
