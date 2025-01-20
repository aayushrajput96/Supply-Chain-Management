# dms/models.py
from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Inventory(models.Model):
    product = models.ForeignKey(
        'oms.Product', 
        on_delete=models.CASCADE, 
        related_name='inventory_records'  # Specify a unique related_name
    )
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

class Return(models.Model):
    order = models.ForeignKey('oms.Order', on_delete=models.CASCADE)
    reason = models.TextField()
    processed = models.BooleanField(default=False)
