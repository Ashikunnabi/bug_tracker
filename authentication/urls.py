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
from django.urls import path

from .views import index_view, login_view, logout_view, registration_view, forgot_pass_view, security_code_view, change_password_view
urlpatterns = [
    path('', index_view, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('registration', registration_view, name='registration'),
    path('forgot', forgot_pass_view, name='forgot_pass'),
    path('confirmation', security_code_view, name='security_code'),
    path('change_password', change_password_view, name='change_password'),
]
