from rest_framework import permissions, viewsets
from merchandise.models import Merchandise, MerchandiseType
from merchandise.serializers import MerchandiseSerializer, MerchandiseTypeSerializer


class MerchandiseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "id"
    queryset = MerchandiseType.objects.all().order_by("-id")
    serializer_class = MerchandiseTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class MerchandiseViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = Merchandise.objects.all().order_by("-created_at")
    serializer_class = MerchandiseSerializer
    permission_classes = permission_classes = [permissions.DjangoModelPermissions]