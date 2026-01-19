from rest_framework import serializers
from staff.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
        read_only_fields = ["updated_at", "created_at", "created_by"]