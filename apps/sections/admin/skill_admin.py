from django.contrib import admin
from ..models.resume import Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "type", "level", "institute"]
    list_editable = ["category", "type", "level"]
    fields = ('name', 'type', 'category', 'institute', 'level')
    list_filter = ["category", "type", "level"]

admin.site.register(Skill, SkillAdmin)