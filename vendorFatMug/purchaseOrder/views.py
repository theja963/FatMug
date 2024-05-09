
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PurchaseOrder
from .forms import PurchaseOrderForm
# Create your views here.
class PurchaseOrderListView(ListView):
    model = PurchaseOrder

class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder   
    def acknowledge(self):
        acknowledgeOrder = self.model.objects.get(pk=self.kwargs['pk'])
        acknowledgeOrder.acknowledgment_date = timezone.now()
        acknowledgeOrder.status = 'acknowledged'
        acknowledgeOrder.save()
    def deliver(self):
        deliverOrder = self.model.objects.get(pk=self.kwargs['pk'])
        deliverOrder.status = 'delivered'
        deliverOrder.deliver_date = timezone.now()
        deliverOrder.quality_rating = 3





class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder

    fields = [
    'po_number',
    'vendor',
    'items',
    'quantity',]
    success_url = reverse_lazy('PurchaseOrder-list')

class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    fields = [
    'po_number',
    'vendor',
    'order_date',
    'delivery_date',
    'items',
    'quantity',
    'status',
    'quality_rating',
    'issue_date',
    'acknowledgment_date'
]
    success_url = reverse_lazy('PurchaseOrder-list')
    

class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    success_url = reverse_lazy('PurchaseOrder-list')

# class PurchaseOrderAcknowledgeView(DetailView):
#     model = PurchaseOrder
    
#     success_url = reverse_lazy('PurchaseOrder-list')

