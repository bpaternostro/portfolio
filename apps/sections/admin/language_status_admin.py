from django.contrib import admin
from ..models.language import LanguageStatus, LanguageStatusLang

class LanguageStatusLangAdmin(admin.TabularInline):
    model = LanguageStatusLang
    extra = 1
    #search_fields = ["routine","day"]
    def __str__(self):
        return f"{self.name}"
    

class LanguageStatusAdmin(admin.ModelAdmin):
    inlines = [
        LanguageStatusLangAdmin,
    ]


admin.site.register(LanguageStatus, LanguageStatusAdmin)