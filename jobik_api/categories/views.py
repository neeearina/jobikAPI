import rest_framework.generics
import rest_framework.viewsets

import categories.models
import categories.serializers

__all__ = [
    "AllCategoriesView",
    "PublishedCategoriesView",
    "CategoryDetailView",
    "CreateCategoryView",
]


class AllCategoriesView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        categories.models.CategoriesModel.objects.all_categories()
    )
    serializer_class = categories.serializers.CategoriesSerializer


class PublishedCategoriesView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        categories.models.CategoriesModel.objects.published_categories()
    )
    serializer_class = categories.serializers.CategoriesSerializer


class CategoryDetailView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    serializer_class = categories.serializers.DetailCategorySerializer

    def get_queryset(self):
        return (
            categories.models.CategoriesModel.objects.category_detail(
                self.kwargs["pk"],
            )
        )


class CreateCategoryView(rest_framework.generics.CreateAPIView):
    queryset = (
        categories.models.CategoriesModel.objects.all()
    )
    serializer_class = categories.serializers.CreateCategorySerializer
