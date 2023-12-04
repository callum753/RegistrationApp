from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address')
    Birthday = forms.DateField(label= 'Birthday')
    Address = forms.CharField(label= 'Address')
    City = forms.CharField(label= 'City')
    Town = forms.CharField(label= 'Town')
    Country = forms.CharField(label= 'Country')
    


class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' , 'Birthday' , 'Address' , 'City' , 'Town' , 'Country']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    Birthday = forms.DateField()
    Address = forms.CharField()
    City = forms.CharField()
    Town = forms.CharField()
    Country = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email' , 'Birthday' , 'Address' , 'City' , 'Town' , 'Country']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']