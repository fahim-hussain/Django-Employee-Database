from .models import Employee, Department


def getEmployeeById(empid):
    return Employee.objects.get(pk=empid)


def appendEmployee(emp):
    empdata = emp.cleaned_data
    print(empdata)
    firstName = empdata['firstName']
    lastName = empdata['lastName']
    email = empdata['email']
    SSN = empdata['SSN']
    addressStreet = empdata['addressStreet']
    addressState = empdata['addressState']
    addressCity = empdata['addressCity']
    addressPostal = empdata['addressPostal']
    isManager = empdata['isManager']
    managerId = empdata['managerId']
    status = empdata['status']
    department = empdata['department']
    hireDate = empdata['hireDate']
    emp = Employee(firstName=firstName, lastName=lastName, email=email, SSN=SSN, addressStreet=addressStreet,
                   addressState=addressState, addressCity=addressCity, addressPostal=addressPostal,
                   isManager=isManager, managerId=managerId, status=status, department=department,
                   hireDate=hireDate)
    emp.save()


def updateEmployee(emp):
    empdata = emp.cleaned_data
    emp = Employee.objects.get(pk=empdata['employeeNum'])

    emp.firstName = empdata['firstName']
    emp.lastName = empdata['lastName']
    emp.email = empdata['email']
    emp.SSN = empdata['SSN']
    emp.addressStreet = empdata['addressStreet']
    emp.addressState = empdata['addressState']
    emp.addressCity = empdata['addressCity']
    emp.addressPostal = empdata['addressPostal']
    emp.isManager = empdata['isManager']
    emp.managerId = empdata['managerId']
    emp.status = empdata['status']
    emp.department = empdata['department']
    emp.hireDate = empdata['hireDate']
    emp.save()


def getEmployeeByStatus(status):
    emp = Employee.objects.all().filter(status=status)
    return emp


def getEmployee():
    return Employee.objects.all()


def getDepartment():
    return Department.objects.all()


def getEmployeeByDepartment(depid):
    depemp = Employee.objects.all().filter(department=depid)
    return depemp


def getEmployeeByManagerId(manid):
    manemp = Employee.objects.all().filter(employeeNum=manid)
    return manemp


def getManager():
    managers = Employee.objects.all().filter(isManager=True)
    return managers


def deleteEmployee(empid):
    employee = Employee.objects.get(pk=empid)
    employee.delete()
