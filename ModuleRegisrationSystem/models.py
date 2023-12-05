from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    Name = models.CharField(max_length = 100)
    Code = models.CharField(max_length = 100)
    Credit = models.CharField(max_length = 100)
    Category = models.CharField(max_length = 100)
    details = models.TextField()
    Availabity = models.CharField(max_length = 100, choices= [('yes', 'yes'), ('no', 'no')])
    #Courses = models.ForeignKey (course, related_name = 'courses',
    
    def __str__(self):
        return f'{self.Name}'

# Create your models here.
