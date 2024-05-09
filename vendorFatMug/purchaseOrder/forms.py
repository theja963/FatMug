# forms.py
import random
from django.utils import timezone
from django import forms
from .models import PurchaseOrder

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['po_number','vendor', 'items', 'quantity']

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderForm, self).__init__(*args, **kwargs)
        # Autofill fields here
        print("autofilling")
        # self.initial['po_number'] = "FM" + str(random.randint(0,1000))+str(random.randint(0,1000))
        self.initial['order_date'] = timezone.now()
        self.initial['status'] = 'pending'  # Example of autofilling the 'status' field
        print('autofilled')
