from django.urls import path
from . import views
from .views import PostListView, PostDetailView, module_registration, StudentRegistration, module_deregistration


app_name = 'ModuleRegisrationSystem'
urlpatterns = [
path('', views.home, name = 'home'),
path('about', views.about, name='about'),
path('contact', views.contact, name='contact' ),
path('registration_list' , views.registration, name='registration'),
path('modules', PostListView.as_view(), name = 'modules'),
path('myregistration', StudentRegistration.as_view(), name='myregistration'),
path('modules/<int:pk>', PostDetailView.as_view(), name ='module-detail'),
path('moduleregistration/<int:pk>/<int:course>', module_registration, name="module-registration"),
path('modulederegistration/<int:pk>/', module_deregistration, name='module-deregistration' )


]