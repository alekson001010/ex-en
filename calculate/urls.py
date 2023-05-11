from django.urls import path
from .views import index, DaysList, DaysDetail


urlpatterns = [
    path('', index, name='index'),
    path('days/', DaysList.as_view(), name='days'),
    path('days/<int:pk>/', DaysDetail.as_view(), name='days_detail'),
]