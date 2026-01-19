import uuid
from django.db import models
from django.contrib.auth import get_user_model
from person.models import Person


class Staff(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="users")
    department = models.TextField(max_length=128, blank=False)
    job_title = models.TextField(max_length=128, blank=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "Staff"
        managed = False
