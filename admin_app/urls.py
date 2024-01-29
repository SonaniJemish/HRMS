from django.urls import path

from . import views


urlpatterns = [
    path("", views.AdminLogin, name="AdminLogin"),
    path("admin_register", views.AdminRegister, name="AdminRegister"),
    path("admin_login", views.AdminLogin, name="AdminLogin"),
    path("admin_index", views.AdminIndex, name="AdminIndex"),
    path("admin_app", views.AdminLogout, name="AdminLogout"),


    path("employee", views.EmployeeDetail, name="Employee"),
    path("employee_list", views.EmployeeList, name="EmployeeList"),
    path("employee/add", views.AddEmployee, name="AddEmployee"),
    path("employee/edit/<int:id>", views.EditEmployee, name="EditEmployee"),
    path("employee/delete/<int:id>", views.DeleteEmployee, name="DeleteEmployee"),
    path("employee_list/delete/<int:id>", views.DeleteEmployeeList, name="DeleteEmployeeList"),


    path("profile/<int:id>", views.Profile, name="Profile"),
    path("profile/detailsform/<int:id>", views.FillProfileDetails, name="FillProfileDetails"),


    path("holidays", views.Holidays, name="Holidays"),
    path("holidays/add", views.AddHolidays, name="AddHolidays"),
    path("holidays/update/<int:id>", views.UpdateHolidays, name="UpdateHoliday"),
    path("holidays/delete/<int:id>", views.DeleteHolidays, name="DeleteHolidays"),

    path("department", views.DepartmentView, name="DepartmentView"),
    path("department/add", views.AddDepartment, name="AddDepartment"),
    # path("department/update/<int:id>", views.UpdateDepartment, name="UpdateDepartment"),
    path("department/delete/<int:id>", views.DeleteDepartment, name="DeleteDepartment"),

    path("designation", views.DesignationView, name="Designation"),
    path("designation/add", views.AddDesignation, name="AddDesignation"),
    # path("designation/update/<int:id>", views.UpdateDesignation, name="UpdateDesignation"),
    path("designation/delete/<int:id>", views.DeleteDesignation, name="DeleteDesignation"),

    # path("edit_holidays", views.test, name="edit_holidays")
]
