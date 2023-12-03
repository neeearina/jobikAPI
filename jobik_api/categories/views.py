import rest_framework.viewsets

import categories.models
import categories.serializers

__all__ = ["PublishedCategoriesView"]


class PublishedCategoriesView(rest_framework.viewsets.ModelViewSet):
    queryset = (
        categories.models.CategoriesModel.objects.published_categories()
    )
    serializer_class = categories.serializers.PublishedCategoriesSerializer
