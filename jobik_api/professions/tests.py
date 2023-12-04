import django.test

import categories.models
import professions.models

__all__ = []


class ProfessionsModelTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="cat1",
        )
        cls.profession1 = professions.models.ProfessionsModel.objects.create(
            name="prof1",
            category=cls.category1,
            wage="2000",
        )

    def test_relations_with_category(self):
        profession = professions.models.ProfessionsModel.objects.get(id=1)
        related_model = profession._meta.get_field("category").related_model
        self.assertEqual(related_model, categories.models.CategoriesModel)
