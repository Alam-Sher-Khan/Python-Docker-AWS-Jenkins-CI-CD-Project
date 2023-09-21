from django.contrib import admin
from .models import ChargeDataRecord
# Register your models here.
@admin.register(ChargeDataRecord)
class CDRadmin(admin.ModelAdmin):
    list_display = ['id','session_identification', 'vehicle_identification', 'start_time', 'end_time', 'total_cost']