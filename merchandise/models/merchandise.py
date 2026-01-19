import uuid
from django.db import models
from django.contrib.auth import get_user_model


MERCHANDISE = ('urn', 'casket', 'flower arragement', 'keepsake book')
MERCHANDISE_CHOICES = (
    ('urn', 'Urn'), 
    ('casket', 'Casket'), 
    ('flower arragement', 'Flower arrangement'), 
    ('keepsake book', 'Keepsake book')
)

class MerchandiseType(models.Model):
    name = models.TextField(max_length=20, unique=True)
    description = models.TextField(max_length=512, blank=False)

    class Meta:
        db_table = "MerchandiseType"
        managed = False

class Merchandise(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    type = models.ForeignKey(MerchandiseType, on_delete=models.PROTECT)
    name = models.TextField(max_length=50, blank=False, unique=True)
    description = models.TextField(max_length=512, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    photo_url = models.TextField(max_length=512, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "Merchandise"
        managed = False