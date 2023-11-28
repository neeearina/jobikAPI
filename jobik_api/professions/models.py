import django.db

__all__ = ["CategoriesModel", "ProfessionsModel"]


class CategoriesModel(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=100,
        help_text="название категории профессии",
        verbose_name="категория",
    )
    description = django.db.models.TextField(
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
