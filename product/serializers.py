from rest_framework import serializers
from product.models import FuneralPackage, FuneralPackageMerchandise


class FuneralPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralPackage
        fields = "__all__"
        read_only_fields = ["created_at",]

class FuneralPackageMerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralPackageMerchandise
        fields = "__all__"