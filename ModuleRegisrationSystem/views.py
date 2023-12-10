from django.shortcuts import render
from .models import Module
from django.views.generic import ListView, DetailView
#from django.contrib.auth.decorators import login_required, user_passes_test

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

class PostListView(ListView):
    model = Module
    template_name = 'ModuleRegisrationSystem/modules.html'
    context_object_name = 'modules'
    ordering = ['Code']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Module




    







