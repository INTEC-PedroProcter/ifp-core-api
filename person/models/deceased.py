import uuid
from django.db import models
from django.contrib.auth import get_user_model
from person.models.person import Person


class Deceased(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    place_of_death = models.TextField(max_length=128, blank=False)
    date_of_death = models.DateField(null=False)
    cause_of_death = models.TextField(max_length=256, blank=False)
    death_certificate_number = models.TextField(max_length=64)
    certified_by = models.TextField(max_length=128)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "Deceased"
        managed = False

    def __str__(self):
        return f'{self.person.names} {self.person.last_names} ({self.person.national_id})'