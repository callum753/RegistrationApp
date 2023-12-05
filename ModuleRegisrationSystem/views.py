from django.shortcuts import render
from .models import Module

def home(request):
    return render(request, 'ModuleRegisrationSystem/home.html', {'title':'Welcome'})
def about(request):
    return render(request, 'ModuleRegisrationSystem/about.html', {'title':'About us'})
def contact(request):
    return render(request, 'ModuleRegisrationSystem/contact.html',{'title':'Contact us'})
def modules(request):
    daily_report = {'Module': Module.objects.all(), 'title': 'Module'}
    return render(request, 'ModuleRegisrationSystem/modules.html', daily_report)
    


# Create your views here.



