from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
# Register your models here.

class SuperAdmin(ModelAdmin):
    admin.site.site_header = admin.site.site_title = "Resume Maker"

all_models = (Master,
User,
Skill,
Education,
Reference,
Experience,
Project,
BoardOrUniversity,
CourseOrStream)

for mdl in all_models:
    admin.site.register(mdl, SuperAdmin)