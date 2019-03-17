from django.db import models


class Employee(models.Model):
    employee_id   = models.CharField(max_length=20)
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20)
    email         = models.EmailField()
    password      = models.CharField(max_length=50)
