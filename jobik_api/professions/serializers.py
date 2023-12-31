import rest_framework.serializers as serializers

import professions.models

__all__ = [
    "ProfessionsSerializer",
    "CreateProfessionSerializer",
    "DetailProfessionSerializer",
    "ProfessionsFromCategorySerializer",
]


class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = professions.models.ProfessionsModel
        fields = [
            professions.models.ProfessionsModel.id.field.name,
            professions.models.ProfessionsModel.name.field.name,
            "category_id",
        ]


class CreateProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = professions.models.ProfessionsModel
        fields = "__all__"


class DetailProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = professions.models.ProfessionsModel
        fields = [
            professions.models.ProfessionsModel.name.field.name,
            professions.models.ProfessionsModel.description.field.name,
            professions.models.ProfessionsModel.wage.field.name,
            "category_id",
        ]


class ProfessionsFromCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = professions.models.ProfessionsModel
        fields = [
            professions.models.ProfessionsModel.name.field.name,
            professions.models.ProfessionsModel.description.field.name,
            professions.models.ProfessionsModel.wage.field.name,
        ]
