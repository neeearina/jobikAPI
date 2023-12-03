from django.apps import AppConfig

__all__ = []


class CategoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "categories"
    verbose_name = "категория"
    verbose_name_plural = "категории"
