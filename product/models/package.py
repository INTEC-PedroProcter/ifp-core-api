import uuid
from django.db import models
from django.contrib.auth import get_user_model


class FuneralType(models.Model):
    name = models.TextField(max_length=20, unique=True)
    service_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)

    class Meta:
        db_table = "FuneralType"
        managed = False

class FuneralPackage(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    type = models.ForeignKey(FuneralType, on_delete=models.PROTECT)
    name = models.TextField(max_length=50, blank=False, unique=True)
    description = models.TextField(max_length=512, blank=False)
    package_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    include_memorial = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "FuneralPackage"
        managed = False