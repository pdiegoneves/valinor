from django.contrib import admin

from project.models.project import Project
from project.models.requirements import Requirements


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "project_manager",
    )
    list_filter = ("project_manager",)
    search_fields = ("name", "description")


@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "requirement_type", "project")
    list_filter = ("requirement_type", "project")
    search_fields = ("name", "description")
