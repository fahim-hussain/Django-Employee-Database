import os.path
import json
from django.conf import settings
from .forms import EmployeeForm

employeeList = []
departmentList = []


def initialize():
    with open(os.path.join(settings.BASE_DIR, 'static/employees.json')) as f:
        global employeeList
        employeeList = json.load(f)

    with open(os.path.join(settings.BASE_DIR, 'static/departments.json')) as f:
        global departmentList
        departmentList = json.load(f)


def getEmployeeById(empid):
    for i in range(len(employeeList)):
        if str(employeeList[i]['employeeNum']) == empid:
            return employeeList[i]


def appendEmployee(emp):
    empdata = emp.cleaned_data
    employeeList.append(empdata)


def updateEmployee(emp):
    empdata = emp.cleaned_data
    print(empdata['employeeNum'])
    for i in range(len(employeeList)):
        if str(employeeList[i]['employeeNum']) == empdata['employeeNum']:
            employeeList[i] = empdata


def getEmployeeByStatus(status):
    emp = []
    for i in range(len(employeeList)):
        if str(employeeList[i]['status']) == status:
            emp.append(employeeList[i])
    return emp


def getEmployee():
    return employeeList


def getDepartment():
    return departmentList


def getEmployeeByDepartment(depid):
    depemp = []
    for i in range(len(employeeList)):
        if str(employeeList[i]['department']) == depid:
            depemp.append(employeeList[i])
    return depemp


def getEmployeeByManagerId(manid):
    manemp = []
    for i in range(len(employeeList)):
        if str(employeeList[i]['employeeManagerNum']) == manid:
            manemp.append(employeeList[i])
    return manemp


def getManager():
    managers = []
    for i in range(len(employeeList)):
        if employeeList[i]['isManager']:
            managers.append(employeeList[i])
    return managers
