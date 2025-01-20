# tms/models.py
from django.db import models

class Carrier(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

class Route(models.Model):
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.FloatField()
    traffic_conditions = models.TextField()

class Shipment(models.Model):
    order = models.ForeignKey('oms.Order', on_delete=models.CASCADE)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Delayed', 'Delayed')],
        default='In Transit'
    )
    updated_at = models.DateTimeField(auto_now=True)
