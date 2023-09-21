
from django.db import models

class ChargeDataRecord(models.Model):
    session_identification = models.CharField(max_length=255)
    vehicle_identification = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

