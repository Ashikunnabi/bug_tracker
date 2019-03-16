from django.contrib import admin
from .models import Bug, Client, Employee, Project


admin.site.register(Bug)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Project)

# Register your models here.
