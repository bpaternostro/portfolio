from django.contrib import admin
from ..models.resume import Experience, Task, Skill
from ..models.language import TaskLang


class TaskLangAdmin(admin.TabularInline):
    model = TaskLang
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ["description"]
    inlines = [
        TaskLangAdmin
    ]

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["company", "title"]

    def get_task_description():
        return [(task, task.description()) for task in Task.objects.all()]


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Task, TaskAdmin)