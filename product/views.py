from django.utils import timezone
from rest_framework import permissions, viewsets, status, response
from product.models import FuneralPackage, FuneralPackageMerchandise
from product.serializers import (
    FuneralPackageSerializer, 
    FuneralPackageMerchandiseSerializer
)


class FuneralPackageViewSet(viewsets.ModelViewSet):
    # lookup_field = "public_id"
    queryset = FuneralPackage.objects.all().order_by("-created_at")
    serializer_class = FuneralPackageSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def create(self, request, *args, **kwargs):
        data = request.data
        data["created_by"] = request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        data["updated_at"] = timezone.now()

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return response.Response(serializer.data)

class FuneralPackageMerchandiseViewSet(viewsets.ModelViewSet):
    queryset = FuneralPackageMerchandise.objects.all().order_by("-id")
    serializer_class = FuneralPackageMerchandiseSerializer
    permission_classes = [permissions.DjangoModelPermissions]