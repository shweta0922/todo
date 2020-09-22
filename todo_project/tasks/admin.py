from django.contrib import admin

# Register your models here.
from django.utils import timezone

from . import models

def mark_complete(model_admin,request,queryset):
    queryset.update(
        status = models.TaskStatus.COMPLETED,
        completed_at = timezone.now()
    )
mark_complete.short_description = "Mark these task as complete"


def mark_pending(models_admin,request,queryset):
    queryset.update(
        status = models.TaskStatus.PENDING,
        completed_at = None
    )
mark_pending.short_description='Mark these task as pending'


class  TaskAdmin(admin.ModelAdmin):
    fields = [
        'content',
        ('deadline','status')
    ]
    list_display = ['content','status','deadline']
    list_editable = ['status']
    actions = [mark_complete,mark_pending]
    list_filter = ['status','deadline','tags']
    search_fields = ['content','tags__name']
    ordering = ['deadline']

admin.site.register(models.Tasks,TaskAdmin)
admin.site.register(models.Tag)