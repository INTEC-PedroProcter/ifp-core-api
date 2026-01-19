from rest_framework import serializers
from person.models import Deceased


class DeceasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deceased
        fields = "__all__"
        read_only_fields = ["updated_at", "created_at", "created_by"]