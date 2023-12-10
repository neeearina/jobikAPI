import http

import django.test
import django.urls
import parameterized

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

    def test_str_method(self):
        profession = professions.models.ProfessionsModel.objects.get(id=1)
        expected_str = f"Профессия {profession.name}"
        self.assertEqual(expected_str, str(profession))


class ProfessionManagerTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="cat1",
        )
        cls.profession1 = professions.models.ProfessionsModel.objects.create(
            name="published profession",
            category=cls.category1,
            wage="2000",
            is_published=True,
        )
        cls.profession2 = professions.models.ProfessionsModel.objects.create(
            name="unpublished profession",
            category=cls.category1,
            wage="2000",
            is_published=False,
        )

    def test_content_in_all_professions(self):
        expected = {"category_id": 1, "id": 2,
                    "name": "unpublished profession",
                    "is_published": False}
        result = (
            professions.models.ProfessionsModel.objects.all_professions()
        )
        self.assertEqual(result.count(), 2)
        self.assertEqual(result[1], expected)

    def test_content_in_published(self):
        expected = {"category_id": 1, "id": 1,
                    "name": "published profession"}
        result = (
            professions.models.ProfessionsModel.objects.published()
        )
        self.assertEqual(result.count(), 1)
        self.assertEqual(result[0], expected)

    @parameterized.parameterized.expand([
        ["id"],
        ["is_published"],
    ])
    def test_content_in_detail(self, unexpected):
        result = (
            professions.models.ProfessionsModel.objects.detail(2)
        )
        self.assertNotIn(unexpected, result)


class ProfessionViewsTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="cat1",
        )
        cls.profession1 = professions.models.ProfessionsModel.objects.create(
            name="published profession",
            category=cls.category1,
            wage="2000",
            is_published=True,
        )
        cls.profession2 = professions.models.ProfessionsModel.objects.create(
            name="unpublished profession",
            category=cls.category1,
            wage="2000",
            is_published=False,
        )

    def test_all_professions(self):
        response = self.client.get(
            django.urls.reverse(
                "professions:all",
            ),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_published(self):
        response = self.client.get(
            django.urls.reverse(
                "professions:published",
            ),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_profession(self):
        num_professions_initial = (
            professions.models.ProfessionsModel.objects.all()
        ).count()
        response_create_profession = self.client.post(
            django.urls.reverse(
                "professions:create_profession",
            ),
            data={"name": "unpublished category 2",
                  "category": "1", "wage": "2000"},
        )
        new_num_professions = (
            professions.models.ProfessionsModel.objects.all()
        ).count()
        self.assertEqual(
            response_create_profession.status_code,
            http.HTTPStatus.CREATED,
        )
        self.assertEqual(
            num_professions_initial + 1,
            new_num_professions,
        )
