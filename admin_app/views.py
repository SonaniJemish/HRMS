from datetime import datetime

from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from hrms_api.models import User, Department, Designation, Holiday


def AdminRegister(request):
    if request.method == "POST":
        adminname = request.POST.get('adminname')
        adminphone = request.POST.get('adminphone')
        adminpassword = request.POST.get('adminpassword')
        admin_details = User(admin_name=adminname, phone=adminphone, password=adminpassword)
        admin_details.save()
        return redirect('/admin_login')
    return render(request, "admin/register.html")


def AdminLogin(request):
    if request.method == "POST":
        adminphone = request.POST.get('adminphone')
        adminpassword = request.POST.get('adminpassword')

        login_data = User.objects.all()
        for x in login_data:
            if x.phone == adminphone:
                if check_password(adminpassword, x.password):
                    return redirect('/admin_index')
    return render(request, "admin/login.html")


def AdminIndex(request):
    return render(request, "admin/index.html")


def AdminLogout(request):
    return render(request, "admin/login.html")


def EmployeeDetail(request):
    employeedetails = User.objects.all()
    return render(request, "admin/employees.html", {'employeedetails': employeedetails})


def EmployeeList(request):
    return render(request, "admin/employees_list.html")


def AddEmployee(request):
    if request.method == "POST":
        employee_name = request.POST.get('employee_name')
        employee_email = request.POST.get('employee_email')
        employee_password = request.POST.get('employee_password')
        employee_phone = request.POST.get('employee_phone')
        employeejoindate = request.POST.get('employee_joindate')
        employee_joindate = datetime.strptime(employeejoindate, '%Y-%m-%d').date()
        employee_department_id = request.POST.get('employee_department')
        employee_department = Department.objects.get(id=employee_department_id)
        employee_designation_id = request.POST.get('employee_designation')
        employee_designation = Designation.objects.get(id=employee_designation_id)
        # if employee_password == employee_conf_password:
        #     emp_verify_password = employee_password
        # else:
        #     print("Password is not match")
        empdetails = User(username=employee_name, email=employee_email, password=employee_password, phone=employee_phone, date_joined=employee_joindate, department=employee_department, designation=employee_designation)
        empdetails.save()
        messages.success(request, "Hello, School data has been send.")
        return redirect('/employee')

    empprofile = User.objects.get(id=id)
    return render(request, "admin/employees.html", {'profile': empprofile})


def EditEmployee(request, id):

    if request.method == "POST":
        up_employee_name = request.POST.get('employee_name')
        up_employee_email =request.POST.get('employee_email')
        up_employee_password = request.POST.get('employee_password')
        up_employee_conf_password = request.POST.get('employee_conf_password')
        up_employee_phone = request.POST.get('employee_phone')
        up_employeejoindate = request.POST.get('employee_joindate')
        up_employee_joindate = datetime.strptime(up_employeejoindate, '%Y-%m-%d').date()
        up_employee_department = request.POST.get('employee_department')
        up_employee_designation = request.POST.get('employee_designation')


        up_empdetails = User.objects.get(id=id)
        up_empdetails.username = up_employee_name
        up_empdetails.email = up_employee_email
        up_empdetails.password = up_employee_password
        up_empdetails.phone = up_employee_phone
        up_empdetails.date_joined = up_employee_joindate
        up_empdetails.department = up_employee_department
        up_empdetails.designation = up_employee_designation
        up_empdetails.save()
        return redirect('/employee')

    edit_employee = User.objects.get(id=id)
    print(edit_employee, ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>PROFILE")
    context = {
        "edit_employee": edit_employee,
    }
    return render(request, "admin/employees.html", context)


def DeleteEmployee(request, id):
    delete_employee = User.objects.get(id=id)
    print(delete_employee.id,">>>>>>>>>>>>>>>>>>>>>>>>>>>DELETE")
    delete_employee.delete()
    if delete_employee not in User:
        print("DATADELETE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return redirect('/employee')
    context = {
        'deleteemployee': delete_employee,
    }
    return render(request, "admin/employees.html", context)


def Profile(request, id):
    profile = User.objects.get(id=id)
    return render(request, "admin/profile.html", {'profile': profile})


def FillProfileDetails(request, id):
    return render(request, "admin/profile.html")


def Holidays(request):
    holidaylist = Holiday.objects.all()
    context = {
        'holidaylist':holidaylist,
    }
    return render(request, "admin/holidays.html", context)


def AddHolidays(request):
    if request.method == 'POST':
        add_holiday_title = request.POST.get('holiday_title')
        add_holiday_date = request.POST.get('holiday_date')
        holiday_add = Holiday(holiday_title=add_holiday_title, holiday_date=add_holiday_date)
        holiday_add.save()
        return redirect('/holidays')
    return render(request, "admin/holidays.html")


def UpdateHolidays(request,id):
    up_holiday_details = Holiday.objects.get(id=id)

    if request.method == 'POST':
        update_holiday_title = request.POST.get('holiday_title')
        update_holiday_date = request.POST.get('holiday_date')
        holiday_add = Holiday(holiday_title=update_holiday_title, holiday_date=update_holiday_date)
        holiday_add.save()
        return redirect('/holidays')

    context = {
        'up_holiday_details':up_holiday_details
    }
    return render(request, "admin/holidays.html",context)


def DepartmentView(request):
    departmentlist = Department.objects.all()
    context = {
        'departmentlist': departmentlist,
    }
    return render(request, "admin/departments.html", context)


def AddDepartment(request):
    if request.method == 'POST':
        add_department_name = request.POST.get('department_name')
        department_add = Department(department_name=add_department_name)
        department_add.save()
        return redirect('/department')
    return render(request, "admin/departments.html")


def DesignationView(request):
    designationlist = Designation.objects.all()
    context = {
        'designationlist': designationlist,
    }
    return render(request, "admin/designations.html", context)