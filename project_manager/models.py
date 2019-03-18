from django.db import models


class Client(models.Model):
    name            = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.name
        
        
class Employee(models.Model):
    STATUS = (
        ('1', 'Married'),
        ('2', 'Unmarried'),
    )
    employee_id          = models.CharField(max_length=50)
    change_password      = models.CharField(max_length=50)
    first_name           = models.CharField(max_length=50)
    last_name            = models.CharField(max_length=50)
    phone_number         = models.CharField(max_length=15)
    email                = models.EmailField()
    present_address      = models.CharField(max_length=200)
    permanent_address    = models.CharField(max_length=200)
    nid                  = models.IntegerField()
    dob                  = models.DateField(auto_now=False, auto_now_add=False)
    designation          = models.CharField(max_length=50)
    skill                = models.CharField(max_length=50)
    marital_status       = models.CharField(max_length=1, choices=STATUS, default='2')    
    
    def __str__(self):
        return self.employee_id
        

class Bug(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

    
class Project(models.Model):
    STATUS = (
        ('1', 'Completed'),
        ('2', 'In Progress'),
    )
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=500, blank=True)
    possible_bugs   = models.ManyToManyField(Bug)
    cost            = models.IntegerField()
    deadline        = models.DateTimeField(auto_now=False, auto_now_add=False)
    status          = models.CharField(max_length=1, choices=STATUS, default='2')
    order_at        = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    
class TaskAssign(models.Model):
    STATUS = (
        ('1', 'Completed'),
        ('2', 'Processing'),
        ('3', 'Failed'),
    )
    project         = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee        = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bugs            = models.ManyToManyField(Bug)
    description     = models.CharField(max_length=500)
    deadline        = models.DateTimeField()
    status          = models.CharField(max_length=1, choices=STATUS, default='2')
    request_id      = models.CharField(max_length=5, blank=True)
    
    def __str__(self):
        return self.project.name

    
class RequestForChange(models.Model):
    PENALTY = (
        ('1', 'Salary Deduction'),
        ('2', 'Overtime'),
    )
    STATUS = (
        ('1', 'Pending'),
        ('2', 'Accepted'),
        ('3', 'Rejected'),
    )
    task            = models.ForeignKey(TaskAssign, on_delete=models.CASCADE)
    penalty         = models.CharField(max_length=1, choices=PENALTY, default='2')
    status          = models.CharField(max_length=1, choices=STATUS, default='1')
    
    def __str__(self):
        return self.task.project.name
        
        
        
