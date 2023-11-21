from django.contrib import admin
from ..models.resume import Education
from ..models.language import EducationLang

class EducationLangAdmin(admin.TabularInline):
    model = EducationLang
    extra = 1

class EducationAdmin(admin.ModelAdmin):
    list_display = ["institute", "title"]
    inlines = [
        EducationLangAdmin
    ]

admin.site.register(Education, EducationAdmin)