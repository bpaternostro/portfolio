from django.contrib import admin
from ..models.resume import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ["full_name", "contact", "subject", "created_on"]

admin.site.register(Message, MessageAdmin)