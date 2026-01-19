from rest_framework import permissions, viewsets
from staff.models import Staff
from staff.serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = Staff.objects.all().order_by("-created_at")
    serializer_class = StaffSerializer
    permission_classes = [permissions.DjangoModelPermissions]