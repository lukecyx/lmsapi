from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .admin_forms import AddUserForm, UpdateUserForm


CustomUser = get_user_model()


class CustomUserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = ("email", "username", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff",)

    fieldsets = (
        ("Account Details", {"fields": ("username", "email", "password")}),
        ("Personal Details", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    search_fields = ("email", "username", "first_name", "surname")
    ordering = ("email", "first_name", "last_name")
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
