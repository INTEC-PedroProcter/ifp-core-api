from django.contrib import admin
from event.models import EventLocation, FuneralEvent

# Register your models here.

admin.site.register(EventLocation)
admin.site.register(FuneralEvent)