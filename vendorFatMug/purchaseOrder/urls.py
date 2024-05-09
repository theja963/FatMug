
# PurchaseOrders/urls.py

from django.urls import path
from .views import PurchaseOrderListView, PurchaseOrderDetailView, PurchaseOrderCreateView, PurchaseOrderUpdateView, PurchaseOrderDeleteView

urlpatterns = [
    path('', PurchaseOrderListView.as_view(), name='PurchaseOrder-list'),
    path('<int:pk>/', PurchaseOrderDetailView.as_view(), name='PurchaseOrder-detail'),
    path('create/', PurchaseOrderCreateView.as_view(), name='PurchaseOrder-create'),
    path('<int:pk>/update/', PurchaseOrderUpdateView.as_view(), name='PurchaseOrder-update'),
    path('<int:pk>/delete/', PurchaseOrderDeleteView.as_view(), name='PurchaseOrder-delete'),
    path('<int:pk>/acknowledge/', PurchaseOrderDetailView.as_view(), name='PurchaseOrder-acknowledge'),
    path('<int:pk>/deliver/', PurchaseOrderDetailView.as_view(), name='PurchaseOrder-deliver'),
]