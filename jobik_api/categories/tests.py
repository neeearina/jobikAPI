import django.test

import categories.models

__all__ = []


class CategoriesManagerTest(django.test.TestCase):
    """Проверка содержимого в методах менеджера категорий"""

    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="cat1",
            link_to_professions="some/link/",
            is_published=True,
        )
        cls.category2 = categories.models.CategoriesModel.objects.create(
            name="cat2",
            link_to_professions="some/link/",
        )

    def test_content_in_published_categories(self):
        expected = {"id": 1, "name": "cat1"}
        profession_urls = (
            categories.models.CategoriesModel.objects.published_categories()
        )
        self.assertEqual(len(profession_urls), 1)
        self.assertEqual(profession_urls[0], expected)

    def test_content_in_all_categories(self):
        expected = {"id": 2, "name": "cat2"}
        profession_urls = (
            categories.models.CategoriesModel.objects.all_categories()
        )
        self.assertEqual(len(profession_urls), 2)
        self.assertEqual(profession_urls[1], expected)
