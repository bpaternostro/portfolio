from django.contrib import admin
from ..models.resume import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "contact"]

admin.site.register(Contact, ContactAdmin)