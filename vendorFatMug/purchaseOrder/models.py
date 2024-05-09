from django.db import models
from vendors.models import Vendor

# Create your models here.
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True)
    delivery_date = models.DateTimeField(null = True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(null = True)
    acknowledgment_date = models.DateTimeField(null=True)