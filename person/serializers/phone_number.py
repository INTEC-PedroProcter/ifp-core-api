from rest_framework import serializers
from person.models import PersonPhoneNumber


class PersonPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonPhoneNumber
        fields = "__all__"
        read_only_fields = ["updated_at", "created_at", "created_by"]