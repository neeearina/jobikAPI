import rest_framework.generics
import rest_framework.viewsets

import categories.models
import categories.serializers

__all__ = ["PublishedCategoriesView"]


class PublishedCategoriesView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        categories.models.CategoriesModel.objects.published_categories()
    )
    serializer_class = categories.serializers.PublishedCategoriesSerializer


class CategoryDetailView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    serializer_class = categories.serializers.DetailCategorySerializer

    def get_queryset(self):
        return (
            categories.models.CategoriesModel.objects.category_detail(
                self.kwargs["pk"],
            )
        )
