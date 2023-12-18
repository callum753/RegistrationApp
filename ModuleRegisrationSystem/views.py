from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Module, User
from django.views.generic import ListView, DetailView , CreateView
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Registration
from .forms import ModuleRegistrationForm

#from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    context = {'courses': Group.objects.all(), 'title': 'Welcome'}
    return render(request, 'ModuleRegisrationSystem/home.html', context)

def about(request):
    return render(request, 'ModuleRegisrationSystem/about.html', {'title':'About us'})
def contact(request):
    return render(request, 'ModuleRegisrationSystem/contact.html',{'title':'Contact us'})
def modules(request):
    daily_report = {'Module': Module.objects.all(), 'title': 'Module'}
    return render(request, 'ModuleRegisrationSystem/modules.html', daily_report)
def registration(request):
    registration_list = Registration.objects.filter(student = request.user)
    print(registration_list)
    return render(request, 'ModuleRegisrationSystem/registration_list.html',{'title': 'My Registrations', 'registrations': registration_list})


class CourseDetailView(DetailView):
    model = Group


# Create your views here.

class PostListView(ListView):
    model = Module
    template_name = 'ModuleRegisrationSystem/modules.html'
    context_object_name = 'modules'
    ordering = ['Code']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Module

#@login_required
def module_registration(request, pk, course):
    module = get_object_or_404(Module, pk=pk)
    if request.method == "POST":
        form = ModuleRegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.module = module
            reg.student = request.user

            reg.save()
            messages.success(request, "You Have Registered")

            #return redirect('ModuleRegisrationSystem:modules', pk=module.id)
            return redirect('course', pk=course)
        else:
            messages.warning(request, "Unable to Register")
            print(f"Forn Errors: {form.errors}")
    else:
        form = ModuleRegistrationForm

    #return redirect('ModuleRegisrationSystem:modules', pk=module.id)
    return redirect('course', pk=course)   

def module_deregistration(request,pk):
    registration = get_object_or_404(Registration,pk=pk)

    if request.user == registration.student:
        registration.delete()
        messages.success(request,f'Module Unregisred!')

    return redirect('ModuleRegisrationSystem:myregistration')




class StudentRegistration(ListView):
    model = Registration
    #template_name = "ModuleRegisrationSystem:student-registrations.html"
    context_object_name = "registrations"

    def get_queryset(self):
        user = get_object_or_404(User, username = self.request.user)
        return Registration.objects.filter(student=user).order_by('module__Name')







    







