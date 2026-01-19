from django.contrib import admin
from merchandise.models import MerchandiseType, Merchandise

# Register your models here.

admin.site.register(MerchandiseType)
admin.site.register(Merchandise)