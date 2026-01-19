from django.contrib import admin
from product.models import FuneralType, FuneralPackage, FuneralPackageMerchandise

# Register your models here.

admin.site.register(FuneralType)
admin.site.register(FuneralPackage)
admin.site.register(FuneralPackageMerchandise)