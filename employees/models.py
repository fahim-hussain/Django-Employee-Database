from django.db import models
from django import forms

# Create your models here.

status = [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
]

department = [
    ('1', 'Creative Services'),
    ('2', 'Product Development'),
    ('3', 'Marketing'),
    ('4', 'Strategic Planning'),
    ('5', 'Accounting'),
    ('6', 'Human Resources'),
    ('7', 'Quality Analysis')
]


class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    SSN = models.CharField(max_length=9)

    addressStreet = models.CharField(max_length=100)
    addressCity = models.CharField(max_length=50)
    addressState = models.CharField(max_length=100)
    addressPostal = models.CharField(max_length=10)

    isManager = models.BooleanField()
    employeeNum = models.IntegerField()
    status = models.CharField(choices=status, max_length=15)
    department = models.CharField(choices=department, max_length=25)
    hireDate = models.DateField(max_length=25)

