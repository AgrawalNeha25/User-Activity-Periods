from rest_framework import serializers
from .models import User, ActivityPeriod
from userActivity import settings

class ActivityPeriodSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data["start_time"] > data["end_time"]:
            raise serializers.ValidationError({"message": "End time should be greater than start time."})
        return data

    start_time = serializers.DateTimeField(format='%b %d %Y %I:%M %p')
    end_time = serializers.DateTimeField(format='%b %d %Y %I:%M %p')

    class Meta:
        model = ActivityPeriod
        fields = ['start_time','end_time']

class UserSerializer(serializers.ModelSerializer):
    settings.TIME_ZONE = User.tz
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ['id','real_name','tz','activity_periods']
