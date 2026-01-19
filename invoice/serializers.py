from rest_framework import serializers
from invoice.models import FuneralInvoice


class FuneralInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralInvoice
        fields = "__all__"

class CreateFuneralInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuneralInvoice
        fields = ["funeral"]