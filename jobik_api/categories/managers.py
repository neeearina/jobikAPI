import django.db.models

__all__ = []


class CategoriesManager(django.db.models.Manager):
    def published_categories(self):
        return (
            self.filter(is_published=True).values("id", "name")
        )
