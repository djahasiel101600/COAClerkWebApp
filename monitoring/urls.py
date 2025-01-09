from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='MonitoringIndex'),
    path('update-iar/<int:pk>/edit/', views.update_iarrecord, name='update-iar'),
]