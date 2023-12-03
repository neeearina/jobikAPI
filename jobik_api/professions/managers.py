import django.db.models

__all__ = ["ProfessionsManager"]


class ProfessionsManager(django.db.models.Manager):
    def all_professions(self):
        return self.values(
            "id",
            "name",
        )
