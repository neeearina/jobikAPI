import django.db.models

__all__ = []


class AbstructModel(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=100,
        help_text="название категории профессии",
        verbose_name="категория",
    )
    description = django.db.models.TextField(
        blank=True,
        help_text="описание категории",
        verbose_name="описание",
    )
    is_published = django.db.models.BooleanField(
        default=False,
        help_text="опубликована категория/профессия или нет",
        verbose_name="опубликовано",
    )

    class Meta:
        verbose_name = "абстрактная модель"
        abstract = True

    def __str__(self):
        return self.name
