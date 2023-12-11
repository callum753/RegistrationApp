from django.contrib import admin
from .models import Module, course, Registration

admin.site.register(Module)
admin.site.register(course)
admin.site.register(Registration)

# Register your models here.
