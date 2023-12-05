import django.contrib.admin
import django.contrib.auth

import users.models

__all__ = []


class ProfileInline(django.contrib.admin.TabularInline):
    model = users.models.Profile
    can_delete = False
    readonly_fields = (
        users.models.Profile.birthday.field.name,
        users.models.Profile.rating.field.name,
    )


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    inlines = (ProfileInline,)


django.contrib.admin.site.unregister(django.contrib.auth.models.User)
django.contrib.admin.site.register(django.contrib.auth.models.User, UserAdmin)
