import uuid
from django.db import models
from django.contrib.auth import get_user_model
from person.models.person import Person


class PhoneNumberType(models.Model):
    name = models.TextField(max_length=20, blank=False)

    class Meta:
        db_table = "PhoneNumberType"
        managed = False

    def __str__(self):
        return self.name

class PersonPhoneNumber(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=128, blank=False)
    type = models.ForeignKey(PhoneNumberType, on_delete=models.PROTECT)
    is_preferred_contact = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "PersonPhoneNumber"
        managed = False

    def __str__(self):
        return f'{self.phone_number} ({self.person.national_id})'