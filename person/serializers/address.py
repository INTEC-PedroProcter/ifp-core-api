from rest_framework import serializers
from person.models import PersonAddress, COUNTRY_CODES_ISO2, INVALID_COUNTRY_CODE_MESSAGE


class PersonAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAddress
        fields = "__all__"
        read_only_fields = ["updated_at", "created_at", "created_by"]

    def validate_country_code(self, value):
        if value not in COUNTRY_CODES_ISO2:
            raise serializers.ValidationError(INVALID_COUNTRY_CODE_MESSAGE)
        
        return value