from rest_framework import permissions, viewsets, decorators
from event.models import EventType, EventLocation, FuneralEvent
from event.serializers import (
    EventTypeSerializer, 
    EventLocationSerializer, 
    FuneralEventSerializer,
    ScheduleFuneralEventSerializer
)


class EventTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventType.objects.all().order_by("-id")
    serializer_class = EventTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventLocationViewSet(viewsets.ModelViewSet):
    # lookup_field = "public_id"
    queryset = EventLocation.objects.all().order_by("-created_at")
    serializer_class = EventLocationSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class FuneralEventViewSet(viewsets.ModelViewSet):
    # lookup_field = "public_id"
    queryset = FuneralEvent.objects.all().order_by("-created_at")
    serializer_class = FuneralEventSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create":
            return ScheduleFuneralEventSerializer
        
        return super().get_serializer_class()