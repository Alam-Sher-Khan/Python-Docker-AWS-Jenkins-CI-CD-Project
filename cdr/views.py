from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import ChargeDataRecord
from .serializers import ChargeDataRecordSerializer


class ChargeDataRecordListCreateView(ListCreateAPIView):
    queryset = ChargeDataRecord.objects.all()
    serializer_class = ChargeDataRecordSerializer
     
class ChargeDataRecordDetailView(RetrieveAPIView):
    queryset = ChargeDataRecord.objects.all()
    serializer_class = ChargeDataRecordSerializer
    
    
    

