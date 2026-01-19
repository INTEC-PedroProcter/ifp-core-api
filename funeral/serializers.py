from rest_framework import serializers
from funeral.models import FuneralStatus, Funeral, FuneralStatusHistory


class FuneralStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralStatus
        fields = "__all__"

class FuneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funeral
        fields = "__all__"

class CreateDraftFuneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funeral
        fields = ["notes", "client", "deceased"]

class AssignFuneralPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funeral
        fields = ["package"]

class FuneralStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralStatusHistory
        fields = "__all__"