from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from .models import Event
from .serializers import EventSerializer
from .tasks import notify_new_event

class EventLCView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        event = serializer.save()
        notify_new_event.delay(event.id)


class EventRetrieveView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"
