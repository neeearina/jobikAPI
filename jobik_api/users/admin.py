import django.contrib.auth.admin

import users.models

__all__ = []


@django.contrib.admin.register(users.models.User)
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    readonly_fields = [
        field.name for field in users.models.User._meta.get_fields()
    ]
    list_display = (
        users.models.User.username.field.name,
        users.models.User.email.field.name,
    )
