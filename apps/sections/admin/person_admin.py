from django.contrib import admin
from ..models.resume import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]

admin.site.register(Person, PersonAdmin)