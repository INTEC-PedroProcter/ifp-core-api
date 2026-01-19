from rest_framework import serializers
from merchandise.models import Merchandise, MerchandiseType


class MerchandiseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchandiseType
        fields = "__all__"

class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = "__all__"
        read_only_fields = ["updated_at", "created_at", "created_by"]