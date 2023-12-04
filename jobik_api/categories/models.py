import django.db.models

import categories.managers
import core.models

__all__ = ["CategoriesModel"]


class CategoriesModel(core.models.AbstractModel):
    objects = categories.managers.CategoriesManager()

    link_to_professions = django.db.models.URLField(
        blank=True,
        max_length=250,
        help_text="ссылка на весь список профессий в данной категории",
        verbose_name="ссылка",
    )
    num_of_professions = django.db.models.PositiveIntegerField(
        default=0,
        help_text="количество профессий в категории",
        verbose_name="количество профессий",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return f"Категория {self.name}"
