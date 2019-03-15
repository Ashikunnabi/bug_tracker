from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Bug, Client, Project
from authentication.decorators import has_access

## ================= INDEX PAGE ==========================
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def index(request):
    """  SUPERUSER and ADMIN has the power to see """   
    context = {
        'project_count': Project.objects.all().count
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

    
    
    
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def employee_add(request):
    """  SUPERUSER and ADMIN has the power to see """
    
    return render(request, 'project_manager/employee_add.html')

   

   
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def employee_details(request):
    """  SUPERUSER and ADMIN has the power to see """
    
    return render(request, 'project_manager/employee_details.html')
    
    
    
    
    
    
    