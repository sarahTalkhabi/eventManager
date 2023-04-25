from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .eventView import EventDetail, EventList, EventAttendee

urlpatterns = [
    path('events/',EventList.as_view(),name='listEvents'),
    path('events/<int:pk>/', EventDetail.as_view(), name='eventviewset'),
    path('attendance/',EventAttendee.as_view()),
    path('attendance/<int:pk>/',EventAttendee.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)