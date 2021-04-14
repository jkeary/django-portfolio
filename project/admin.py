from django.contrib import admin
from .models import Project, ProjectType

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectType)