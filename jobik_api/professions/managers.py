import django.db.models

__all__ = []


class CategoriesManager(django.db.models.Manager):
    def professions_urls(self):
        return self.values("id", "link_to_professions")

    def published_categories(self):
        return self.values("id", "name", "is_published")
