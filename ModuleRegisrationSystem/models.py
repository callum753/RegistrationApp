from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    type = models.CharField(max_length = 100 , choices =[('Designing cloud based system', 'Designing cloud based system'), ('Advanced date managment', 'Advanced date managment')])
    room = models.CharField(max_length = 100)
    details = models.TextField()
    author = models.ForeignKey(User, related_name = 'Module',
    on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.type} Module in {self.room}'

# Create your models here.
