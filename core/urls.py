"""
URL configuration for ifp_core_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from person.views import (
    PersonViewSet, 
    PersonPhoneNumberViewSet, 
    PersonAddressViewSet, 
    DeceasedViewSet
)
from staff.views import StaffViewSet
from merchandise.views import MerchandiseViewSet, MerchandiseTypeViewSet
from product.views import (
    FuneralPackageViewSet, 
    FuneralPackageMerchandiseViewSet
)
from funeral.views import (
    FuneralViewSet, 
    FuneralStatusViewSet, 
    FuneralStatusHistoryViewSet
)
from event.views import (
    EventTypeViewSet,
    EventLocationViewSet,
    FuneralEventViewSet
)
from invoice.views import FuneralInvoiceViewSet
from payment.views import (
    PaymentViewSet, 
    PaymentMethodViewSet, 
    PaymentStatusViewSet
)
from core.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'people', PersonViewSet)
router.register(r'deceased', DeceasedViewSet)
router.register(r'staffs', StaffViewSet)
router.register(r'phone-numbers', PersonPhoneNumberViewSet)
router.register(r'addresses', PersonAddressViewSet)
router.register(r'merchandise-types', MerchandiseTypeViewSet)
router.register(r'merchandise', MerchandiseViewSet)
router.register(r'packages', FuneralPackageViewSet)
router.register(r'packages-merchandise', FuneralPackageMerchandiseViewSet)
router.register(r'funerals', FuneralViewSet)
router.register(r'funerals-status', FuneralStatusViewSet)
router.register(r'funerals-status-history', FuneralStatusHistoryViewSet)
router.register(r'events-types', EventTypeViewSet)
router.register(r'events-locations', EventLocationViewSet)
router.register(r'events', FuneralEventViewSet)
router.register(r'invoices', FuneralInvoiceViewSet)
router.register(r'payments-methods', PaymentMethodViewSet)
router.register(r'payments-status', PaymentStatusViewSet)
router.register(r'payments', PaymentViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
