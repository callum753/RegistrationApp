from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            course = form.cleaned_data.get('group')

            course = Group.objects.get(id = course.id) 
            user.groups.add(course)
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account!')
            messages.warning(request, f'user) from Errors; {form.errors}')
        context ={'form' : form, 'errors': form.errors} 
        return render(request, 'users/register.html', context)
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form , 'title': 'Module Registration'})

# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        u_form.save()
        p_form.save()
        messages.success(request, 'Your account has been successfully updated')
        return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        context = {'u_form': u_form, 'p_form': p_form, 'title': 'User Profile'}
        return render(request, 'users/profile.html', context)



