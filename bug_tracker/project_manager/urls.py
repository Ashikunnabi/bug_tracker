"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='pm_index'),
    
    path('project/add', project_add, name='pm_project_add'),
    path('project/detail/<int:id>', project_details, name='pm_project_details'),
    path('project/delete/<int:id>', project_delete, name='pm_project_delete'),
    
    path('bug/add', bug_add, name='pm_bug_add'),
    path('bug/detail/<int:id>', bug_details, name='pm_bug_details'),
    path('bug/delete/<int:id>', bug_delete, name='pm_bug_delete'),
    
    path('client/add', client_add, name='pm_client_add'),
    path('client/detail/<int:id>', client_details, name='pm_client_details'),
    path('client/delete/<int:id>', client_delete, name='pm_client_delete'),
    
    path('employee/add', employee_add, name='pm_employee_add'),
    path('employee/detail', employee_details, name='pm_employee_details'),
]
