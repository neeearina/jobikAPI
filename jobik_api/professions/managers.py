import django.db.models

__all__ = ["ProfessionsManager"]


class ProfessionsManager(django.db.models.Manager):
    def all_professions(self):
        return self.values(
            "id",
            "name",
            "category_id",
        )

    def published(self):
        return self.filter(is_published=True).values(
            "id",
            "name",
            "category_id",
        )

    def detail(self, pk):
        return self.filter(pk=pk).values(
            "name",
            "description",
            "wage",
            "category_id",
        )
