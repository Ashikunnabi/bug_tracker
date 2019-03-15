from django.db import models


class Client(models.Model):
    name            = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.name

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
    project         = models.ForeignKey(Project, on_delete=models.CASCADE)
    description     = models.CharField(max_length=500)
    possible_bugs   = models.ManyToManyField(Bug)
    cost            = models.IntegerField()
    deadline        = models.DateField()
    
    def __str__(self):
        return self.name
        
        
        
