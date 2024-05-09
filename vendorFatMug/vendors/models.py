from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=15)
    on_time_delivery_rate = models.FloatField(max_length=15)
    quality_rating_avg = models.FloatField(max_length=15)
    average_response_time = models.IntegerField(max_length=15)
    fulfilment_rate = models.IntegerField(max_length=15)
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'vendors'