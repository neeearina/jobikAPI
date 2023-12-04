from django.apps import AppConfig

__all__ = []


class ProfessionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "professions"
    verbose_name = "профессия"
    verbose_name_plural = "профессии"
