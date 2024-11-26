from django.contrib import admin
from .models import Task

#para ver fecha de creacion aunque no se defina por el usuario en el panel admin
class TaskAdmin(admin.ModelAdmin):
    readonly_fields=("created",)
# Register your models here.
admin.site.register(Task, TaskAdmin)