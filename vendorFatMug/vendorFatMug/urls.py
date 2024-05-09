from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/', include('vendors.urls')),
    path('purchaseOrder/', include('purchaseOrder.urls')),
]