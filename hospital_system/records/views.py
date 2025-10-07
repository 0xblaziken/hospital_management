from django.shortcuts import render, redirect
from .models import Patient, Employee

def index(request):
    return render(request, 'records/index.html')

def patients(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        Patient.objects.create(name=name, age=age, gender=gender)
        return redirect('patients')
    data = Patient.objects.all()
    return render(request, 'records/patients.html', {'patients': data})

def employees(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        Employee.objects.create(name=name, role=role)
        return redirect('employees')
    data = Employee.objects.all()
    return render(request, 'records/employees.html', {'employees': data})

def add_patient(request):
    return render(request, 'records/add_patient.html')

def add_employee(request):
    return render(request, 'records/add_employee.html')
