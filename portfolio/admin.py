from django.contrib import admin
from .models import Profile, Sckill, Project
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "headline", "email")

@admin.register(Sckill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech", "is_published", "created_at")
    list_editable = ("is_published",)
    list_filter = ("is_published",)
    search_fields = ("title", "description", "tech")