from django.utils import timezone
from rest_framework import permissions, viewsets, decorators, response, status
from funeral.models import Funeral, FuneralStatus, FuneralStatusHistory
from funeral.serializers import (
    FuneralSerializer, 
    CreateDraftFuneralSerializer,
    AssignFuneralPackageSerializer,
    FuneralStatusSerializer, 
    FuneralStatusHistorySerializer
)


class FuneralViewSet(viewsets.ModelViewSet):
    # lookup_field = "public_id"
    queryset = Funeral.objects.all().order_by("-created_at")
    serializer_class = FuneralSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "create_draft_funeral_case":
            return CreateDraftFuneralSerializer
        
        if self.action == "assign_package":
            return AssignFuneralPackageSerializer

        return super().get_serializer_class()
    
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

    @decorators.action(url_path="create-draft", methods=["POST"], detail=False)
    def create_draft_funeral_case(self, request, pk=None):
        pass

    @decorators.action(url_path="assign-package", methods=["POST"], detail=True)
    def assign_package(self, request, public_id):
        pass

    @decorators.action(url_path="mark-completed", methods=["GET"], detail=True)
    def mark_completed(self, request, public_id):
        pass

    @decorators.action(url_path="mark-closed", methods=["GET"], detail=True)
    def mark_closed(self, request, public_id):
        pass

    @decorators.action(url_path="mark-cancelled", methods=["GET"], detail=True)
    def mark_cancelled(self, request, public_id):
        pass

class FuneralStatusViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "id"
    queryset = FuneralStatus.objects.all().order_by("-id")
    serializer_class = FuneralStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class FuneralStatusHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "id"
    queryset = FuneralStatusHistory.objects.all().order_by("-id")
    serializer_class = FuneralStatusHistorySerializer
    permission_classes = [permissions.DjangoModelPermissions]