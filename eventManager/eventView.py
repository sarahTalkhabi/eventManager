from datetime import timezone, datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, mixins, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import time
from .models import Event, Attendance
from .serializers import eventSerializer,attendanceSerializer


from rest_framework.request import Request

class EventList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,format=None):
        events = Event.objects.all()
        serializer = eventSerializer(events, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = eventSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save(creator =self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self,pk):
        try:
            return Event.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = eventSerializer(events)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
            if event.creator != request.user.id:
                return Response('You are not authorized to change this event.', status=status.HTTP_401_UNAUTHORIZED)
            serializer = eventSerializer(event, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventAttendee(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        userEvents = Attendance.objects.filter( attendee=self.request.user.id, is_attending=True)
        serializer = attendanceSerializer(userEvents, many=True)
        return Response(serializer.data)
    def post(self, request, pk,format=None):
        serializer = attendanceSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save( attendee=self.request.user.id,is_attending=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            attendance = Attendance.objects.get(pk=pk)
            if time.mktime(attendance.event.startDate.timetuple()) <= time.mktime(datetime.now().timetuple()):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            attendance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
