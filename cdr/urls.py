from django.urls import path
from cdr import views
urlpatterns = [
    path('', views.ChargeDataRecordListCreateView.as_view()),
    path('<int:pk>/', views.ChargeDataRecordDetailView.as_view()),
]
