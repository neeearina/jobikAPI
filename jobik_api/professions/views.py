import rest_framework.generics as generics
import rest_framework.viewsets as viewsets

import professions.models
import professions.paginations
import professions.serializers

__all__ = [
    "AllProfessionsView",
    "PublishedProfessionsView",
    "CreateProfessionView",
    "ProfessionDetailView",
]


class AllProfessionsView(viewsets.ReadOnlyModelViewSet):
    queryset = (
        professions.models.ProfessionsModel.objects.all_professions()
    )
    serializer_class = professions.serializers.ProfessionsSerializer
    pagination_class = professions.paginations.ProfessionsPagination


class PublishedProfessionsView(viewsets.ReadOnlyModelViewSet):
    queryset = (
        professions.models.ProfessionsModel.objects.published()
    )
    serializer_class = professions.serializers.ProfessionsSerializer
    pagination_class = professions.paginations.ProfessionsPagination


class CreateProfessionView(generics.CreateAPIView):
    queryset = (
        professions.models.ProfessionsModel.objects.all()
    )
    serializer_class = professions.serializers.CreateProfessionSerializer


class ProfessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = professions.serializers.DetailProfessionSerializer

    def get_queryset(self):
        return (
            professions.models.ProfessionsModel.objects.detail(
                self.kwargs["pk"],
            )
        )


class ProfessionsFromCategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = (
        professions.serializers.ProfessionsFromCategorySerializer
    )
    pagination_class = professions.paginations.ProfessionsPagination

    def get_queryset(self):
        return (
            professions.models.ProfessionsModel.objects.from_category(
                self.kwargs["category_id"],
            )
        )
