from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User

from .models import Bug, Client, Employee, Project, TaskAssign
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
    return render(request, 'project_manager/index.html', context)

    
    
## ================= PROJECT ADD ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def project_add(request):
    """  SUPERUSER and ADMIN has the power to add new project """
    success_message, error_message = None, None
    projects = Project.objects.all()
    bugs     = Bug.objects.all()
    clients  = Client.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        company_name         = request.POST['company_name']
        project_name         = request.POST['project_name']
        project_description  = request.POST['project_description']
        possible_bugs        = request.POST.getlist('possible_bugs')
        testing_cost         = request.POST['testing_cost']
        deadline_date        = request.POST['deadline_date']
        deadline_time        = request.POST['deadline_time']        
        deadline             = deadline_date+" "+deadline_time
        # Creating new project
        try:
            project   = Project.objects.create(
                            client=Client.objects.get(id=company_name),
                            name=project_name,
                            description=project_description,
                            cost=testing_cost,
                            deadline=deadline
                        )
            project.possible_bugs.set(possible_bugs)
            project.save()
            success_message =  "new project added."
        except Exception as e:
            print(e)
            error_message = "to add project."        
    
    context = {
        'projects'        : projects,
        'bugs'            : bugs,
        'clients'         : clients,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    return render(request, 'project_manager/project_add.html', context)

   

## ================= PROJECT DETAIL - UPDATE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def project_details(request, id):
    """  Project detail with editible form will be shown """
    success_message, error_message = None, None    
    project = Project.objects.get(id=id)
    bugs    = Bug.objects.all()
    clients = Client.objects.all()    
    
    # Catching POST request 
    if request.method == "POST":
        company_name         = request.POST['company_name']
        project_name         = request.POST['project_name']
        project_description  = request.POST['project_description']
        possible_bugs        = request.POST.getlist('possible_bugs')
        testing_cost         = request.POST['testing_cost']
        deadline_date        = request.POST['deadline_date']
        deadline_time        = request.POST['deadline_time']        
        deadline             = deadline_date+" "+deadline_time
        # Creating new project
        try:
            project.client      = Client.objects.get(id=company_name)
            project.name        = project_name
            project.description = project_description
            project.cost        = testing_cost
            project.deadline    = deadline
            project.possible_bugs.set(possible_bugs)
            project.save()
            success_message     = "project updated."
        except Exception as e:
            print(e)
            error_message       = "to update project."
    
    context = {
        'project'         : project,
        'bugs'            : bugs,
        'clients'         : clients,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    
    return render(request, 'project_manager/project_details.html', context)

    
    
## ================= PROJECT DELETE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def project_delete(request, id):
    """  Project can be deleted """
    success_message, error_message = None, None    
    project  = Project.objects.get(id=id)
    projects = Project.objects.all()
    bugs     = Bug.objects.all()
    clients  = Client.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        # Creating new project
        try:
            project.delete()
            success_message =  "project deleted."
        except Exception as e:
            print(e)
            error_message = "to delete project." 
    
    context = {
        'projects'        : projects,
        'bugs'            : bugs,
        'clients'         : clients,
        'success_message' : success_message,
        'error_message'   : error_message,
    }    
    return render(request, 'project_manager/project_add.html', context)



## ================= BUG ADD ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def bug_add(request):
    """  SUPERUSER and ADMIN has the power to add new bug """
    success_message, error_message = None, None
    bugs     = Bug.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        bug_name         = request.POST['bug_name']
        bug_description  = request.POST['bug_description']
        # Creating new project
        try:
            bug   = Bug.objects.create(
                      name=bug_name,
                      description=bug_description,
                    )
            bug.save()
            success_message =  "new bug added."
        except Exception as e:
            print(e)
            error_message = "to add bug."        
    
    context = {
        'bugs'            : bugs,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    return render(request, 'project_manager/bug_add.html', context)

   

## ================= BUG DETAIL - UPDATE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def bug_details(request, id):
    """  Bug detail with editible form will be shown """
    success_message, error_message = None, None    
    bug = Bug.objects.get(id=id)
    
    # Catching POST request 
    if request.method == "POST":
        bug_name         = request.POST['bug_name']
        bug_description  = request.POST['bug_description']
        # Creating new project
        try:
            bug.name        = bug_name
            bug.description = bug_description
            bug.save()
            success_message =  "bug updated."
        except Exception as e:
            print(e)
            error_message = "to update bug."
    
    context = {
        'bug'             : bug,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    
    return render(request, 'project_manager/bug_details.html', context)

    
    
## ================= BUG DELETE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def bug_delete(request, id):
    """  Bug can be deleted """
    success_message, error_message = None, None    
    bug  = Bug.objects.get(id=id)
    bugs = Bug.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        # Creating new project
        try:
            bug.delete()
            success_message =  "project deleted."
        except Exception as e:
            print(e)
            error_message = "to delete project." 
    
    context = {
        'bugs'            : bugs,
        'success_message' : success_message,
        'error_message'   : error_message,
    }    
    return render(request, 'project_manager/bug_add.html', context)



## ================= CLIENT ADD ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def client_add(request):
    """  SUPERUSER and ADMIN has the power to add new client """
    success_message, error_message = None, None
    clients     = Client.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        client_name          = request.POST['client_name']
        client_phone_number  = request.POST['client_phone_number']
        # Creating new project
        try:
            client   = Client.objects.create(
                      name=client_name,
                      phone_number=client_phone_number,
                    )
            client.save()
            success_message =  "new client added."
        except Exception as e:
            print(e)
            error_message = "to add client."        
    
    context = {
        'clients'         : clients,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    return render(request, 'project_manager/client_add.html', context)

   

## ================= CLIENT DETAIL - UPDATE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def client_details(request, id):
    """  Client detail with editible form will be shown """
    success_message, error_message = None, None    
    client = Client.objects.get(id=id)
    
    # Catching POST request 
    if request.method == "POST":
        client_name          = request.POST['client_name']
        client_phone_number  = request.POST['client_phone_number']
        # Creating new project
        try:
            client.name         = client_name
            client.phone_number = client_phone_number
            client.save()
            success_message =  "client updated."
        except Exception as e:
            print(e)
            error_message = "to update client." 
    
    context = {
        'client'          : client,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    
    return render(request, 'project_manager/client_details.html', context)

    
    
## ================= CLIENT DELETE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def client_delete(request, id):
    """  client can be deleted """
    success_message, error_message = None, None    
    client  = Client.objects.get(id=id)
    clients = Client.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        # Creating new project
        try:
            client.delete()
            success_message =  "client deleted."
        except Exception as e:
            print(e)
            error_message   = "to delete client." 
    
    context = {
        'clients'         : clients,
        'success_message' : success_message,
        'error_message'   : error_message,
    }    
    return render(request, 'project_manager/client_add.html', context)


    
    
## ================= EMPLOYEE ADD ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def employee_add(request):
    """  SUPERUSER and ADMIN has the power to add new employee """
    success_message, error_message = None, None
    employees     = Employee.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        employee_id        = request.POST['employee_id']
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
        # Creating new project
        try:
            employee   = Employee.objects.create(
                      employee_id=employee_id,
                      change_password=change_password,
                      first_name=first_name,
                      last_name=last_name,
                      phone_number=phone_number,
                      email=email,
                      present_address=present_address,
                      permanent_address=permanent_address,
                      nid=nid,
                      dob=dob,
                      designation=designation,
                      skill=skill,
                      marital_status=marital_status,
                    )
            employee.save()
            user = User.objects.create_user(employee_id, email, change_password)
            user.save()
            # Add employee to a 'employee' group
            group = Group.objects.get(name='employee')
            group.user_set.add(user)  
            success_message =  "new employee added."
        except Exception as e:
            print(e)
            error_message = "to add employee."        
    
    context = {
        'employees'       : employees,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    return render(request, 'project_manager/employee_add.html', context)

   

## ================= EMPLOYEE DETAIL - UPDATE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def employee_details(request, id):
    """  employee detail with editible form will be shown """
    success_message, error_message = None, None    
    employee = Employee.objects.get(id=id)
    # Catching POST request 
    if request.method == "POST":
        employee_id        = request.POST['employee_id']
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
        # Creating new project
        try:            
            # employee.employee_id        = employee_id      
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
            success_message =  "employee updated."
        except Exception as e:
            print(e)
            error_message = "to update employee."    
    
    context = {
        'employee'        : employee,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    
    return render(request, 'project_manager/employee_details.html', context)

    
    
## ================= EMPLOYEE DELETE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def employee_delete(request, id):
    """  employee can be deleted """
    success_message, error_message = None, None    
    employee  = Employee.objects.get(id=id)
    employees = Employee.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        # Creating new project
        try:
            user = User.objects.get(username=employee.employee_id)            
            user.delete()
            employee.delete()
            success_message =  "employee deleted."
        except Exception as e:
            print(e)
            error_message   = "to delete employee." 
    
    context = {
        'employees'       : employees,
        'success_message' : success_message,
        'error_message'   : error_message,
    }    
    return render(request, 'project_manager/employee_add.html', context)

    

## ================= TASK ADD ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def task_add(request):
    """  SUPERUSER and ADMIN has the power to add new client """
    success_message, error_message = None, None
    projects  = Project.objects.all()
    employees = Employee.objects.all()
    tasks     = TaskAssign.objects.all()
    bugs      = Bug.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        project          = request.POST['project_name']
        employee         = request.POST['employee_name']
        bugs             = request.POST.getlist('bugs')
        description      = request.POST['description']
        deadline_date    = request.POST['deadline_date']
        deadline_time    = request.POST['deadline_time']        
        deadline         = deadline_date+" "+deadline_time
        # Creating new project
        try:
            task   = TaskAssign.objects.create(
                      project=Project.objects.get(id=project),
                      employee=Employee.objects.get(id=employee),
                      description=description,
                      deadline=deadline,
                    )
            task.bugs.set(bugs)
            task.save()
            success_message =  "new task added."
        except Exception as e:
            print(e)
            error_message = "to add task."        
    
    context = {
        'projects'        : projects,
        'employees'       : employees,
        'tasks'           : tasks,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    return render(request, 'project_manager/task_add.html', context)

   

## ================= TASK DETAIL - UPDATE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def task_details(request, id):
    """  Client detail with editible form will be shown """
    success_message, error_message = None, None    
    task = TaskAssign.objects.get(id=id)
    project = Project.objects.get(id=task.project.id)
    
    # Catching POST request 
    if request.method == "POST":
        employee         = request.POST['employee_name']
        bugs             = request.POST.getlist('bugs')
        description      = request.POST['description']
        deadline_date    = request.POST['deadline_date']
        deadline_time    = request.POST['deadline_time']        
        deadline         = deadline_date+" "+deadline_time
        task_status      = request.POST['task_status']
        # Creating new project
        try:
            task.employee    = Employee.objects.get(id=employee)
            task.description = description
            task.deadline    = deadline
            task.status      = task_status
            task.bugs.set(bugs)
            task.save()
            success_message =  "task updated."
        except Exception as e:
            print(e)
            error_message = "to update task." 
    
    context = {
        'task'            : task,
        'employees'       : Employee.objects.all(),
        'bugs'            : project.possible_bugs.all,
        'success_message' : success_message,
        'error_message'   : error_message,
    }
    
    return render(request, 'project_manager/task_details.html', context)

    
    
## ================= TASK DELETE ==========================   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def task_delete(request, id):
    """  employee can be deleted """
    success_message, error_message = None, None    
    task  = TaskAssign.objects.get(id=id)
    tasks = TaskAssign.objects.all()
    
    # Catching POST request 
    if request.method == "POST":
        # Creating new project
        try:          
            task.delete()
            success_message =  "task deleted."
        except Exception as e:
            print(e)
            error_message   = "to delete task." 
    
    context = {
        'tasks'           : tasks,
        'success_message' : success_message,
        'error_message'   : error_message,
    }    
    return render(request, 'project_manager/task_add.html', context)    

    
    
    
    
    
    