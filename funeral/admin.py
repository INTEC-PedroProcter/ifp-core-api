from django.contrib import admin
from funeral.models import FuneralStatus, Funeral, FuneralStatusHistory

# Register your models here.

admin.site.register(FuneralStatus)
admin.site.register(Funeral)
admin.site.register(FuneralStatusHistory)