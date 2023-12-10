import django.contrib.auth.models
import django.db.models

import users.managers

__all__ = ["User"]


class User(django.contrib.auth.models.AbstractUser):
    objects = users.managers.UserManager()

    birthday = django.db.models.DateField(
        null=True,
        help_text="дата рождения пользователя",
        verbose_name="дата рождения",
        blank=True,
    )
    rating = django.db.models.PositiveIntegerField(
        default=0,
        help_text="рейтинг пользователя в тестах на проф. ориентацию",
        verbose_name="рейтинг",
    )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ["username"]

    def __str__(self):
        return f"Пользователь {self.username}"
