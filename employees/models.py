from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
    firstName = models.CharField(max_length=50, verbose_name="First Name")
    lastName = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    SSN = models.CharField(max_length=11, verbose_name="Social Security Number")

    addressStreet = models.CharField(max_length=100, verbose_name="Street")
    addressCity = models.CharField(max_length=50, verbose_name="City")
    addressState = models.CharField(max_length=100, verbose_name="State")
    addressPostal = models.CharField(max_length=10, verbose_name="Postal Code")

    isManager = models.BooleanField(verbose_name="Manager")
    employeeNum = models.IntegerField(primary_key=True, verbose_name="Employee Number")
    managerId = models.IntegerField(blank=True, null=True, verbose_name="Manager Id")
    status = models.CharField(choices=status, max_length=15, verbose_name="Status")
    department = models.CharField(choices=department, max_length=25, verbose_name="Department")
    hireDate = models.DateField(max_length=25, verbose_name="Hire Date")


class Department(models.Model):
    deptId = models.IntegerField(primary_key=True)
    departmentName = models.CharField(max_length=30)


