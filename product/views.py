from rest_framework import permissions, viewsets
from product.models import FuneralPackage, FuneralPackageMerchandise
from product.serializers import (
    FuneralPackageSerializer, 
    FuneralPackageMerchandiseSerializer
)


class FuneralPackageViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = FuneralPackage.objects.all().order_by("-created_at")
    serializer_class = FuneralPackageSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class FuneralPackageMerchandiseViewSet(viewsets.ModelViewSet):
    queryset = FuneralPackageMerchandise.objects.all().order_by("-id")
    serializer_class = FuneralPackageMerchandiseSerializer
    permission_classes = [permissions.DjangoModelPermissions]