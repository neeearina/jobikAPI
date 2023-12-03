import rest_framework.serializers as serializers

import categories.models

__all__ = ["PublishedCategoriesSerializer"]


class PublishedCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories.models.CategoriesModel
        fields = [
            categories.models.CategoriesModel.id.field.name,
            categories.models.CategoriesModel.name.field.name,
            categories.models.CategoriesModel.is_published.field.name,
        ]


class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories.models.CategoriesModel
        fields = [
            categories.models.CategoriesModel.name.field.name,
            categories.models.CategoriesModel.description.field.name,
            categories.models.CategoriesModel.num_of_professions.field.name,
            categories.models.CategoriesModel.is_published.field.name,
        ]
