import uuid
from django.db import models
from django.contrib.auth import get_user_model
from funeral.models import Funeral


class FuneralInvoice(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    funeral = models.ForeignKey(Funeral, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    tax = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    is_closed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "FuneralInvoice"
        managed = False