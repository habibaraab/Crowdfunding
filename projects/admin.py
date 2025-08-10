# projects/admin.py

from django.contrib import admin
from .models import Project, Donation, Profile 

admin.site.register(Project)
admin.site.register(Donation)
admin.site.register(Profile) 