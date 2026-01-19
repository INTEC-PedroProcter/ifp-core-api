from rest_framework import permissions, viewsets
from person.models import Person, PersonAddress, PersonPhoneNumber, Deceased
from person.serializers import (
    PersonSerializer, 
    PersonAddressSerializer, 
    PersonPhoneNumberSerializer, 
    DeceasedSerializer
)


class PersonViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = Person.objects.all().order_by("-created_at")
    serializer_class = PersonSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class PersonAddressViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = PersonAddress.objects.all().order_by("-created_at")
    serializer_class = PersonAddressSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class PersonPhoneNumberViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = PersonPhoneNumber.objects.all().order_by("-created_at")
    serializer_class = PersonPhoneNumberSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class DeceasedViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    queryset = Deceased.objects.all().order_by("-created_at")
    serializer_class = DeceasedSerializer
    permission_classes = [permissions.DjangoModelPermissions]