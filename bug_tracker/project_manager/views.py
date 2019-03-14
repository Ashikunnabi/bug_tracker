from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Bug, Client, Project
from authentication.decorators import has_access


# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def index(request):
    """  SUPERUSER and ADMIN has the power to see """
    
    return render(request, 'project_manager/index.html')

    
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def project_add(request):
    """  SUPERUSER and ADMIN has the power to see """
    
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'project_manager/project_add.html', context)

    
# @login_required(login_url='login')
# @has_access(allowed_roles=['superuser', 'admin'])
def project_details(request, id):
    """  Project detail with editible form will be shown """
    
    project = Project.objects.get(id=id)
    bugs = Bug.objects.all()
    context = {
        'project': project,
        'bugs': bugs,
    }
    
    return render(request, 'project_manager/project_details.html', context)

    
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
    
    
    
    
    
    
    