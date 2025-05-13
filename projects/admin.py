from django.contrib.gis import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.GISModelAdmin):
    list_display = ('name', 'code', 'status', 'start_date', 'end_date', 'budget')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('name', 'code', 'description', 'address')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'code', 'description', 'status')
        }),
        ('时间和预算', {
            'fields': ('start_date', 'end_date', 'budget')
        }),
        ('位置信息', {
            'fields': ('location', 'address')
        }),
        ('系统信息', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
