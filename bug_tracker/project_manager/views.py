from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentication.decorators import has_access


@login_required(login_url='login')
@has_access(allowed_roles=['superuser', 'admin'])
def index(request):
    """  SUPERUSER and ADMIN has the power to see """
    
    return render(request, 'project_manager/index.html')