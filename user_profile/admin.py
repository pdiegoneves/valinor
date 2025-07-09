from django.contrib import admin

from user_profile.models.user_profile import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
