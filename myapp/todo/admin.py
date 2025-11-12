from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_at', 'due_date')
    list_filter = ('status', 'priority')
    search_fields = ('title',)
