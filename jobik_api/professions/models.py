import django.db.models

import categories.models
import core.models
import professions.managers

__all__ = ["ProfessionsModel"]


class ProfessionsModel(core.models.AbstractModel):
    objects = professions.managers.ProfessionsManager()

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
        ordering = ["name"]

    def __str__(self):
        return f"Профессия {self.name}"
