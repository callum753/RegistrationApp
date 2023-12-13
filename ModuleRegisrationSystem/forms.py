from django import forms
from .models import Registration

class ModuleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['student','module']