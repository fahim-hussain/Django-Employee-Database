from django.urls import path
from . import views

urlpatterns = [
    path('addEmployee/', views.addEmployee),
    path('Employee/', views.employeesPage),
    path('Employee/<empid>', views.employeeDetail),
    path('Department/', views.departments),
    path('employee/department/<depid>', views.departmentEmployee),
    path('employee/manager/<manid>', views.managerEmployee),
    path('employee/status/<status>', views.statusEmployee),
    path('Managers/', views.managers),
    path('', views.homepage)
]
