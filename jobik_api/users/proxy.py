import django.contrib.auth.models

import users.managers

__all__ = ["User"]


class User(django.contrib.auth.models.User):
    objects = users.managers.UserManager()

    class Meta:
        proxy = True

    def __str__(self):
        return f"Пользователь {self.username}"
