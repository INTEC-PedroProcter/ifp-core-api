from rest_framework import serializers
from event.models import EventType, EventLocation, FuneralEvent


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"

class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = "__all__"

class FuneralEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralEvent
        fields = "__all__"

class ScheduleFuneralEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralEvent
        fields = ["type", "funeral", "start_at", "ends_at", "location"]
