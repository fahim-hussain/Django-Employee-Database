from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .dataService import *


initialize()


# Create your views here.
def homepage(request):
    return render(request, 'employees/home.html')


def employeesPage(request):
    employees = getEmployee()
    return render(request, 'employees/employees.html', {'employees': employees})


def employeeDetail(request, empid):
    employees = getEmployeeById(empid)
    if request.method == 'POST':
        emp = EmployeeForm(request.POST)

        if emp.is_valid():
            updateEmployee(emp)
            return employeesPage(request)
        else:
            form = EmployeeForm(request.POST)
            return render(request, 'employees/employeeDetail.html', {'form': form})
    else:
        form = EmployeeForm(employees)

        return render(request, 'employees/employeeDetail.html', {'form': form})


def statusEmployee(request, status):
    employees = getEmployeeByStatus(status)
    return render(request, 'employees/employees.html', {'employees': employees})


def departments(request):
    department = getDepartment()
    return render(request, 'employees/department.html', {'department': department})


def departmentEmployee(request, depid):
    employees = getEmployeeByDepartment(depid)
    return render(request, 'employees/employees.html', {'employees': employees})


def managerEmployee(request, manid):
    employees = getEmployeeByManagerId(manid)
    return render(request, 'employees/employees.html', {'employees': employees})


def managers(request):
    managers = getManager()
    return render(request, 'employees/employees.html', {'employees': managers})


def addEmployee(request):
    if request.method == 'POST':
        emp = EmployeeForm(request.POST)

        if emp.is_valid():
            appendEmployee(emp)
            return employeesPage(request)
        else:
            form = EmployeeForm(request.POST)
            return render(request, 'employees/addEmployee.html', {'form': form})
    else:
        form = EmployeeForm()
        return render(request, 'employees/addEmployee.html', {'form': form})
