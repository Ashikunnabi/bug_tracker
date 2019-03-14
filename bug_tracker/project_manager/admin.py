from django.contrib import admin
from .models import Bug, Client, Project


admin.site.register(Bug)
admin.site.register(Client)
admin.site.register(Project)

# Register your models here.
