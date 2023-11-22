from django.shortcuts import render

def home(request):
    return render(request, 'ModuleRegisrationSystem/home.html')
def about(request):
    return render(request, 'ModuleRegisrationSystem/about.html')
def contact(request):
    return render(request, 'ModuleRegisrationSystem/contact.html')
def modules (request):
    return render(request, 'ModuleRegisrationSystem/modules.html')
    


# Create your views here.
