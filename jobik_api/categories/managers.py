import django.db.models

__all__ = []


class CategoriesManager(django.db.models.Manager):
    def published_categories(self):
        return (
            self.filter(is_published=True).values(
                "id",
                "name",
            )
        )

    def category_detail(self, pk):
        return (
            self.filter(pk=pk).values(
                "name",
                "description",
                "is_published",
                "num_of_professions",
            )
        )
