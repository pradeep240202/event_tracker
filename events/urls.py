from django.urls import path
from .views import EventLCView,EventRetrieveView

urlpatterns = [
    path("events/",EventLCView.as_view(),name="events_lc"),
    path("events/<int:id>",EventRetrieveView.as_view(),name="event_rud"),
]

