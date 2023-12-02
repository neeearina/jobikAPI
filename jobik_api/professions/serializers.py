import rest_framework.serializers as serializers

import professions.models

__all__ = ["PublishedCategoriesSerializer"]


class PublishedCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = professions.models.CategoriesModel
        fields = [
            professions.models.CategoriesModel.id.field.name,
            professions.models.CategoriesModel.name.field.name,
            professions.models.CategoriesModel.is_published.field.name,
        ]
