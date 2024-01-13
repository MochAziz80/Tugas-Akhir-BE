from django.contrib import admin
from django.urls import path, include
from Sepatu.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produk', ProductViewset)
router.register('customer', CustomerViewset)
router.register('order', OrderViewset)
router.register('orderItem', OrderItemViewset)

urlpatterns = [
    path('', include('Sepatu.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
