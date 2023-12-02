import rest_framework.viewsets

import professions.models
import professions.serializers

__all__ = ["PublishedCategoriesView"]


class PublishedCategoriesView(rest_framework.viewsets.ModelViewSet):
    queryset = (
        professions.models.CategoriesModel.objects.published_categories()
    )
    serializer_class = professions.serializers.PublishedCategoriesSerializer
