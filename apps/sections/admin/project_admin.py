from django.contrib import admin
from ..models.resume import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "summary"]

admin.site.register(Project, ProjectAdmin)