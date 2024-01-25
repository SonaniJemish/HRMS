from django.urls import path

from . import views


urlpatterns = [
    path("", views.AdminLogin, name="AdminLogin"),
    path("admin_register", views.AdminRegister, name="AdminRegister"),
    path("admin_login", views.AdminLogin, name="AdminLogin"),
    path("admin_index", views.AdminIndex, name="AdminIndex"),
    path("",views.AdminLogout, name="AdminLogout"),

    path("profile/<int:id>", views.Profile, name="Profile"),

    path("employee", views.EmployeeDetail, name="Employee"),
    path("employee_list", views.EmployeeList, name="EmployeeList"),
    path("employee/add", views.AddEmployee, name="AddEmployee"),
    path("employee/edit/<int:id>", views.EditEmployee, name="EditEmployee"),
    path("employee/delete/<int:id>", views.DeleteEmployee, name="DeleteEmployee"),

]