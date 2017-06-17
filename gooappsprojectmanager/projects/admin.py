from django.contrib import admin

# Register your models here.
from .models import Project, TypeProject, StatusProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeProject)
class TypeProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(StatusProject)
class StatusProjectAdmin(admin.ModelAdmin):
    pass

