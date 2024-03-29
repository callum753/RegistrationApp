from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.contrib.auth.models import Group

class course(models.Model):
    name = models.CharField(max_length= 30 , primary_key= 'name')
    startdate = models.DateField(default = timezone.now)
    duration = models.CharField(max_length= 10 , choices=[('1 year' , '1 year'), ('2 year' , '2 year'), ('3 year' , '3 year'), ])
    details = models.TextField()

    def __str__(self):
        return f'{self.name}'



class Module(models.Model):
    Name = models.CharField(max_length = 100)
    Code = models.CharField(max_length = 100)
    Credit = models.CharField(max_length = 100)
    Category = models.CharField(max_length = 100)
    details = models.TextField()
    Availbity = models.CharField(max_length= 100, choices= [('yes', 'yes'), ('no', 'no')],default= 'yes')
    Groups = models.ManyToManyField(Group,related_name= 'modules')


    
    def __str__(self):
        return f'{self.Name}'
    
class Registration(models.Model):
    student = models.ForeignKey(User,null= True, related_name= 'student', on_delete= models.CASCADE)
    module = models.ForeignKey(Module, null = True, related_name= 'module', on_delete= models.CASCADE)
    dOfRegistration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} is assigned to {self.module}'


# Create your models here.
