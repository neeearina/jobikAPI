import rest_framework.generics as generics
import rest_framework.viewsets

import professions.models
import professions.paginations
import professions.serializers

__all__ = [
    "AllProfessionsView",
    "PublishedProfessionsView",
    "CreateProfessionView",
    "ProfessionDetailView",
]


class AllProfessionsView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        professions.models.ProfessionsModel.objects.all_professions()
    )
    serializer_class = professions.serializers.ProfessionsSerializer
    pagination_class = professions.paginations.ProfessionsPagination


class PublishedProfessionsView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        professions.models.ProfessionsModel.objects.published()
    )
    serializer_class = professions.serializers.ProfessionsSerializer
    pagination_class = professions.paginations.ProfessionsPagination


class CreateProfessionView(rest_framework.generics.CreateAPIView):
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
