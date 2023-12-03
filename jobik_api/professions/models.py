import django.db.models

import categories.models
import core.models

__all__ = ["ProfessionsModel"]


class ProfessionsModel(core.models.AbstructModel):
    wage = django.db.models.CharField(
        max_length=100,
        help_text="заработная плата",
        verbose_name="заработная плата",
    )
    category = django.db.models.ForeignKey(
        categories.models.CategoriesModel,
        on_delete=django.db.models.CASCADE,
        help_text="к какой категории относится профессия",
    )

    class Meta:
        verbose_name = "профессия"
        verbose_name_plural = "профессии"
