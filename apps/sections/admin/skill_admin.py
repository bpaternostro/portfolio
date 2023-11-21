from django.contrib import admin
from ..models.resume import Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "type", "level"]
    list_editable = ["category", "type", "level"]
    fields = ('name', 'type', 'category', 'institute', 'is_soft', 'is_lang', 'level')
    list_filter = ["category", "type", "level"]

admin.site.register(Skill, SkillAdmin)