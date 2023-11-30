import django.db.models

import professions.managers

__all__ = ["CategoriesModel", "ProfessionsModel"]


class CategoriesModel(django.db.models.Model):
    objects = professions.managers.CategoriesManager()
    name = django.db.models.CharField(
        max_length=100,
        help_text="название категории профессии",
        verbose_name="категория",
    )
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
    description = django.db.models.TextField(
        blank=True,
        help_text="описание категории",
        verbose_name="описание",
    )
    is_published = django.db.models.BooleanField(
        default=False,
        help_text="опубликована категория или нет",
        verbose_name="опубликовано",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class ProfessionsModel(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=100,
        help_text="название профессии",
        verbose_name="название",
    )
    description = django.db.models.TextField(
        help_text="описание профессии",
        verbose_name="описание",
    )
    wage = django.db.models.CharField(
        max_length=100,
        help_text="заработная плата",
        verbose_name="заработная плата",
    )
    is_published = django.db.models.BooleanField(
        default=False,
        help_text="опубликована профессия или нет",
        verbose_name="опубликовано",
    )
    category = django.db.models.ForeignKey(
        CategoriesModel,
        on_delete=django.db.models.CASCADE,
        help_text="к какой категории относится профессия",
    )

    class Meta:
        verbose_name = "профессия"
        verbose_name_plural = "профессии"

    def __str__(self):
        return self.name
