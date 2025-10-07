from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    admitted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
