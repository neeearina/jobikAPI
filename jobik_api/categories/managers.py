import django.db.models

__all__ = ["CategoriesManager"]


class CategoriesManager(django.db.models.Manager):
    def professions_urls(self):
        return self.values("id", "link_to_professions")

    def all_categories(self):
        return (
            self.values(
                "id",
                "name",
                "is_published",
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
