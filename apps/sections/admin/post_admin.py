from django.contrib import admin
from ..models.resume import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "summary", "like", "share", "view"]

admin.site.register(Post, PostAdmin)