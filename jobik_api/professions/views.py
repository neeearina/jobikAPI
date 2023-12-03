import rest_framework.viewsets

import professions.models
import professions.paginations
import professions.serializers

__all__ = []


class AllProfessionsView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        professions.models.ProfessionsModel.objects.all_professions()
    )
    serializer_class = professions.serializers.AllProfessionsSerializer
    pagination_class = professions.paginations.ProfessionsPagination


class PublishedProfessionsView(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = (
        professions.models.ProfessionsModel.objects.published_professions()
    )
    serializer_class = professions.serializers.AllProfessionsSerializer
    pagination_class = professions.paginations.ProfessionsPagination
