from django.contrib import admin
from person.models import MaritalStatus, Person, PersonAddress, PersonPhoneNumber, Deceased

# Register your models here.

admin.site.register(MaritalStatus)
admin.site.register(Person)
admin.site.register(PersonAddress)
admin.site.register(PersonPhoneNumber)
admin.site.register(Deceased)