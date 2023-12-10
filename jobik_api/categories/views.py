import rest_framework.generics as generics
import rest_framework.viewsets as viewsets

import categories.models
import categories.serializers

__all__ = [
    "AllCategoriesView",
    "PublishedCategoriesView",
    "CategoryDetailView",
]


class AllCategoriesView(generics.ListCreateAPIView):
    queryset = (
        categories.models.CategoriesModel.objects.all_categories()
    )
    serializer_class = categories.serializers.CategoriesSerializer


class PublishedCategoriesView(viewsets.ReadOnlyModelViewSet):
    queryset = (
        categories.models.CategoriesModel.objects.published()
    )
    serializer_class = categories.serializers.CategoriesSerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = categories.serializers.DetailCategorySerializer

    def get_queryset(self):
        return (
            categories.models.CategoriesModel.objects.detail(
                self.kwargs["pk"],
            )
        )
