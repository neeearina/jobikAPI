import django.db.models

import core.models
import professions.managers

__all__ = ["CategoriesModel", "ProfessionsModel"]


class CategoriesModel(core.models.AbstructModel):
    objects = professions.managers.CategoriesManager()

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


class ProfessionsModel(core.models.AbstructModel):
    wage = django.db.models.CharField(
        max_length=100,
        help_text="заработная плата",
        verbose_name="заработная плата",
    )
    category = django.db.models.ForeignKey(
        CategoriesModel,
        on_delete=django.db.models.CASCADE,
        help_text="к какой категории относится профессия",
    )

    class Meta:
        verbose_name = "профессия"
        verbose_name_plural = "профессии"
