import django.conf
import django.db.models

__all__ = ["Profile"]


class Profile(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        help_text="пользователь",
        verbose_name="пользователь",
    )
    birthday = django.db.models.DateField(
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
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    def __str__(self):
        return f"Пользователь {self.user}"
