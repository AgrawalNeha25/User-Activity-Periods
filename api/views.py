from .models import User, ActivityPeriod
from rest_framework import viewsets
from .serializers import UserSerializer, ActivityPeriodSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    serializer_class = ActivityPeriodSerializer
    queryset = ActivityPeriod.objects.all()



