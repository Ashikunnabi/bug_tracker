from django.shortcuts import render
from django.contrib.auth.models import User

from project_manager.models import Bug, Client, Employee, Project, TaskAssign
from authentication.decorators import has_access



## ================= INDEX PAGE ==========================
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def index(request):
    """  SUPERUSER and ADMIN has the power to see """  
    context = {
        'project_count': Project.objects.all().count,
        'client_count': Client.objects.all().count,
        'employee_count': Employee.objects.all().count,
    }    
    return render(request, 'employee/index.html', context)

    

## ================= PROFILE PAGE ==========================
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def profile(request):
    """  SUPERUSER and ADMIN has the power to see """ 
    success_message, error_message = None, None    
    print("g",request.user.username)  
    employee = Employee.objects.get(employee_id=request.user.username)
    if request.method == "POST":
        first_name         = request.POST['first_name']
        last_name          = request.POST['last_name']
        phone_number       = request.POST['phone_number']
        email              = request.POST['email']
        present_address    = request.POST['present_address']
        permanent_address  = request.POST['permanent_address']
        nid                = request.POST['nid']
        dob                = request.POST['dob']
        designation        = request.POST['designation']
        skill              = request.POST['skill']
        change_password    = request.POST['change_password']
        marital_status     = request.POST['marital_status']
        # Update employee profile
        try:                 
            employee.first_name         = first_name       
            employee.last_name          = last_name        
            employee.phone_number       = phone_number     
            employee.email              = email            
            employee.present_address    = present_address  
            employee.permanent_address  = permanent_address
            employee.nid                = nid              
            employee.dob                = dob              
            employee.designation        = designation      
            employee.skill              = skill            
            employee.change_password    = change_password  
            employee.marital_status     = marital_status   
            employee.save()
            user = User.objects.get(username=employee.employee_id)
            user.email=email
            user.set_password(change_password)
            user.save()
            success_message =  "profile updated."
        except Exception as e:
            print(e)
            error_message = "to update profile." 
    
    context = {
        'employee': employee,
        'success_message' : success_message,
        'error_message'   : error_message,
    }    
    return render(request, 'employee/employee_details.html', context)

    
    
## ================= TASK_SET PAGE ==========================
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def task_set(request):
    """  SUPERUSER and ADMIN has the power to see """ 
    employee = Employee.objects.get(employee_id=request.user.username)
    # Query for employee task which is in processing
    tasks = TaskAssign.objects.filter(employee_id=employee.id, status='2')
    context = {
        'tasks': tasks,
    }    
    return render(request, 'employee/task_sets.html', context)

    

## ================= TASK DETAILS PAGE ==========================
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def task_details(request, id):
    """  SUPERUSER and ADMIN has the power to see """ 
    employee = Employee.objects.get(employee_id=request.user.username)
    # Query for employee task which is in processing
    task = TaskAssign.objects.get(id=id)
    context = {
        'task': task,
    }    
    return render(request, 'employee/task_details.html', context)
    
    
    
    
    
    
    
    
    
    
