from rest_framework import permissions, viewsets
from payment.models import Payment, PaymentStatus, PaymentMethod
from payment.serializers import (
    PaymentSerializer, 
    CreatePaymentSerializer,
    PaymentStatusSerializer, 
    PaymentMethodSerializer
)


class PaymentMethodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentMethod.objects.all().order_by("-id")
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentStatus.objects.all().order_by("-id")
    serializer_class = PaymentStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = Payment.objects.all().order_by("-created_at")
    serializer_class = PaymentSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create":
            return CreatePaymentSerializer
        
        return super().get_serializer_class()