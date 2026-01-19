from django.db import models
from product.models.package import FuneralPackage
from merchandise.models import Merchandise


class FuneralPackageMerchandise(models.Model):
    package = models.ForeignKey(FuneralPackage, on_delete=models.CASCADE)
    merchandise = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=False)

    class Meta:
        db_table = "FuneralPackageMerchandise"
        managed = False