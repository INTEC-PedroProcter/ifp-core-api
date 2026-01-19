import uuid
from django.db import models
from django.contrib.auth import get_user_model
from funeral.models import Funeral


class EventType(models.Model):
    name = models.TextField(max_length=50, blank=False)

    class Meta:
        db_table = "EventType"
        managed = False

    def __str__(self):
        return self.name

class EventLocation(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=512, blank=False)
    photo_url = models.TextField(max_length=512, blank=True)
    max_capacity = models.IntegerField(default=1, null=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "EventLocation"
        managed = False

    def __str__(self):
        return self.name

class FuneralEvent(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    type = models.ForeignKey(EventType, on_delete=models.PROTECT)
    funeral = models.ForeignKey(Funeral, on_delete=models.CASCADE)
    location = models.ForeignKey(EventLocation, on_delete=models.PROTECT)
    start_at = models.DateTimeField(null=False)
    ends_at = models.DateTimeField(null=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "FuneralEvent"
        managed = False

    def __str__(self):
        return self.public_id.hex