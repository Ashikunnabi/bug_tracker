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
    path('', index, name='em_index' ),
    
    path('profile', profile, name='em_profile'),
    path('tasks', task_set, name='em_task_set'),
    path('task/detail/<int:id>', task_details, name='em_task_details'),
    path('request', request_for_change, name='em_request_for_change'),
    # path('project/delete/<int:id>', project_delete, name='pm_project_delete'),
]
