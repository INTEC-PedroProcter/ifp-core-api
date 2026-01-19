from django.contrib import admin
from payment.models import FuneralInvoice, PaymentMethod, PaymentStatus, Payment

# Register your models here.

admin.site.register(PaymentMethod)
admin.site.register(PaymentStatus)
admin.site.register(Payment)