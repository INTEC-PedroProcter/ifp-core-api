import uuid
from django.db import models
from django.contrib.auth import get_user_model
from person.models import Person, Deceased
from product.models import FuneralPackage


class FuneralStatus(models.Model):
    name = models.TextField(max_length=20, unique=True)
    description = models.TextField(max_length=512)

    class Meta:
        db_table = "FuneralStatus"
        managed = False

    def __str__(self):
        return self.name

class Funeral(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    package = models.ForeignKey(FuneralPackage, on_delete=models.PROTECT, null=True)
    client = models.ForeignKey(Person, on_delete=models.PROTECT)
    deceased = models.ForeignKey(Deceased, on_delete=models.PROTECT)
    status = models.ForeignKey(FuneralStatus, on_delete=models.PROTECT)
    notes = models.TextField(max_length=512)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "Funeral"
        managed = False
        permissions = [
            ("can_assign_funeral_package", "Can assign a package to a funeral"),
            ("can_cancel_funeral", "Can cancel a funeral"),
            ("can_close_funeral", "Can close a funeral"),
            ("can_complete_funeral", "Can mark a funeral as completed")
        ]

    def __str__(self):
        return self.public_id.hex

class FuneralStatusHistory(models.Model):
    funeral = models.ForeignKey(Funeral, on_delete=models.CASCADE)
    past_status = models.ForeignKey(FuneralStatus, on_delete=models.PROTECT, related_name="past_status")
    new_status = models.ForeignKey(FuneralStatus, on_delete=models.PROTECT, related_name="new_status")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "FuneralStatusHistory"
        managed = False

    def __str__(self):
        return str(self.created_at)
