from django.contrib import admin

from user_profile.models.register_user import RegisterUser


@admin.register(RegisterUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email",)
