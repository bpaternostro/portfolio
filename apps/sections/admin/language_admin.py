from django.contrib import admin
from ..models.language import Language

class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)