import uuid
from django.db import models
from django.contrib.auth import get_user_model


NATIONAL_ID_TYPES = ('C', 'P')
NATIONAL_ID_TYPE_CHOICES = (('C', 'Cedula'), ('P', 'Passport'))
GENDERS = ('M', 'F', 'O')
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))

class MaritalStatus(models.Model):
    name = models.TextField(max_length=20, unique=True)

    class Meta:
        db_table = "MaritalStatus"
        managed = False

    def __str__(self):
        return self.name

class Person(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    national_id = models.TextField(max_length=20, unique=True, blank=False)
    national_id_type = models.TextField(max_length=1, default='C', null=False, choices=NATIONAL_ID_TYPE_CHOICES)
    names = models.TextField(max_length=50, blank=False)
    last_names = models.TextField(max_length=100, blank=False)
    gender = models.TextField(max_length=1, blank=False, choices=GENDER_CHOICES)
    birthday = models.DateField(null=False)
    birth_place = models.TextField(max_length=128)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT)
    occupation = models.TextField(max_length=64)
    photo_url = models.TextField(max_length=512, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        db_table = "Person"
        managed = False
        constraints = [
            models.CheckConstraint(
                condition=models.Q(gender__in=GENDERS),
                name="CK_Person_Valid_Gender",
                violation_error_message="Gender must be one of this values: 'M', 'F' or 'O'."
            ),
            models.CheckConstraint(
                condition=models.Q(national_id_type=NATIONAL_ID_TYPES),
                name="CK_Person_Valid_National_ID_Type",
                violation_error_message="National ID type must be one of this values: 'C' or 'P'."
            ),
        ]

    def __str__(self):
        return f'{self.names} {self.last_names} ({self.national_id})'