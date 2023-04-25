from rest_framework import serializers
from .models import Event,Attendance
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'startDate', 'endDate', 'creator']


class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['event','attendee','is_attending']