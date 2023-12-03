import django.test

import categories.models

__all__ = []


class CategoriesManagerTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="cat1",
            link_to_professions="some/link/",
        )
        cls.category2 = categories.models.CategoriesModel.objects.create(
            name="cat2",
            link_to_professions="some/link/",
        )

    def test_content_in_method(self):
        """Какие поля возвращает метод professions_urls в менеджере"""
        expected = {"id": 1, "link_to_professions": "some/link/"}
        profession_urls = (
            categories.models.CategoriesModel.objects.professions_urls()
        )
        self.assertEqual(profession_urls[0], expected)
