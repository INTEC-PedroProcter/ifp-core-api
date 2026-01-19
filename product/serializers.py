from rest_framework import serializers
from product.models import FuneralPackage, FuneralPackageMerchandise


class FuneralPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralPackage
        fields = "__all__"
        read_only_fields = ["updated_at", "created_at", "created_by"]

class FuneralPackageMerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralPackageMerchandise
        fields = "__all__"