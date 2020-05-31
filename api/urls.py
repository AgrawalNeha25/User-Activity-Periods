from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet, ActivityPeriodViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('activePeriods',ActivityPeriodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
