from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vendor
from django.template  import loader

# Create your views here.
class VendorListView(ListView):
    
    model = Vendor

class VendorDetailView(DetailView):
    model = Vendor

class VendorCreateView(CreateView):
    model = Vendor
    fields = ['name', 'contact_details', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
    'average_response_time',
    'fulfilment_rate']
    success_url = reverse_lazy('vendor-list')

class VendorUpdateView(UpdateView):
    model = Vendor
    fields = ['name', 'contact_details', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
    'average_response_time',
    'fulfilment_rate']
    
    success_url = reverse_lazy('vendor-list')
    

class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendor-list')