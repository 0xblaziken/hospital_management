from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('patients/', views.patients, name='patients'),
    path('employees/', views.employees, name='employees'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_employee/', views.add_employee, name='add_employee'),
]
