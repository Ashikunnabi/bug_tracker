from django.contrib import admin
from .models import Bug, Client, Employee, Project, TaskAssign


admin.site.register(Bug)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(TaskAssign)

# Register your models here.
