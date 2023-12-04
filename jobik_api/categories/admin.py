import django.contrib

import categories.models

__all__ = []


@django.contrib.admin.register(categories.models.CategoriesModel)
class CategoriesAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        categories.models.CategoriesModel.name.field.name,
        categories.models.CategoriesModel.is_published.field.name,
    )
    list_editable = (
        categories.models.CategoriesModel.is_published.field.name,
    )
    list_display_links = (
        categories.models.CategoriesModel.name.field.name,
    )
