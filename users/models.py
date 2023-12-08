from django.db import models

from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    birthday = models.DateField(null = True)
    address = models.CharField(null = True, max_length= 30)
    city = models.CharField(null = True, max_length= 20)
    town = models.CharField(null = True, max_length= 20)
    country = models.CharField(null = True, max_length= 20)
    image = models.ImageField(default = 'pexels-photo-771742.webp', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

# Create your models here.
