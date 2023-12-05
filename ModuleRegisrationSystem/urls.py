from django.urls import path
from . import views
from .views import PostListView, PostDetailView

app_name = 'ModuleRegisrationSystem'
urlpatterns = [
path('', views.home, name = 'home'),
path('about', views.about, name='about'),
path('contact', views.contact, name='contact' ),
path('modules', PostListView.as_view(), name = 'modules'),
path('modules/<int:pk>', PostDetailView.as_view(), name ='module-detail')
]