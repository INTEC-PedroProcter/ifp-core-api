import uuid
from django.db import models
from django.contrib.auth import get_user_model
from invoice.models import FuneralInvoice


class PaymentMethod(models.Model):
    name = models.TextField(max_length=11, unique=True)

    class Meta:
        db_table = "PaymentMethod"
        managed = False

class PaymentStatus(models.Model):
    name = models.TextField(max_length=9, unique=True)

    class Meta:
        db_table = "PaymentStatus"
        managed = False

class Payment(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    invoice = models.ForeignKey(FuneralInvoice, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    status = models.ForeignKey(PaymentStatus, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    notes = models.TextField(max_length=512)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "Payment"
        managed = False