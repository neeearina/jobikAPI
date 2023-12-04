import django.db.models

__all__ = ["CategoriesManager"]


class CategoriesManager(django.db.models.Manager):
    def all_categories(self):
        return (
            self.values(
                "id",
                "name",
            )
        )

    def published(self):
        return (
            self.filter(is_published=True).values(
                "id",
                "name",
            )
        )

    def detail(self, pk):
        return (
            self.filter(pk=pk).values(
                "name",
                "description",
                "is_published",
                "num_of_professions",
            )
        )
