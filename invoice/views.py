from rest_framework import permissions, viewsets
from invoice.models import FuneralInvoice
from invoice.serializers import (
    FuneralInvoiceSerializer, 
    CreateFuneralInvoiceSerializer
)


class FuneralInvoiceViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = FuneralInvoice.objects.all().order_by("-created_at")
    serializer_class = FuneralInvoiceSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateFuneralInvoiceSerializer

        return super().get_serializer_class()