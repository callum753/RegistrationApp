from django.shortcuts import render

def home(request):
    return render(request, 'ModuleRegisrationSystem/home.html', {'title':'Welcome'})
def about(request):
    return render(request, 'ModuleRegisrationSystem/about.html', {'title':'About us'})
def contact(request):
    return render(request, 'ModuleRegisrationSystem/contact.html',{'title}':'Contact us'})
def modules (request):
    return render(request, 'ModuleRegisrationSystem/modules.html', {'title':'modules'})
    


# Create your views here.



