from rest_framework import serializers
from .models import ChargeDataRecord

class ChargeDataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeDataRecord
        fields = '__all__'
        
    def validate(self, data):
        if data['end_time'] < data['start_time']:
            raise serializers.ValidationError("End time cannot be smaller than Start time")
        
        if data['total_cost'] <= 0:
            raise serializers.ValidationError("Total cost must be greater than 0")
        
        vehicle_id = data['vehicle_identification']
        start_time = data['start_time']
        
        # Check if there are any previous records for the same vehicle
        previous_records = ChargeDataRecord.objects.filter(
            vehicle_identification=vehicle_id,
            #end_time__gte=start_time  # Use "greater than or equal" for end time comparison
        )
        
        if previous_records.exists():
            max_previous_end_time = previous_records.latest('end_time').end_time
            if start_time <= max_previous_end_time:
                raise serializers.ValidationError("Start time can not be smaller that previous session end time")
        
        return data   
