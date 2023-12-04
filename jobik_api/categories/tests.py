import http

import django.test
import django.urls
import parameterized

import categories.models

__all__ = []


class CategoriesModelTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="cat1",
        )

    def test_str_method(self):
        category = categories.models.CategoriesModel.objects.get(id=1)
        expected_str = f"Категория {category.name}"
        self.assertEqual(expected_str, str(category))


class CategoriesManagerTest(django.test.TestCase):
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

    def test_content_in_published(self):
        expected = {"id": 1, "name": "cat1"}
        profession_urls = (
            categories.models.CategoriesModel.objects.published()
        )
        self.assertEqual(profession_urls.count(), 1)
        self.assertEqual(profession_urls[0], expected)

    def test_content_in_all_categories(self):
        expected = {"id": 2, "name": "cat2"}
        profession_urls = (
            categories.models.CategoriesModel.objects.all_categories()
        )
        self.assertEqual(profession_urls.count(), 2)
        self.assertEqual(profession_urls[1], expected)

    @parameterized.parameterized.expand([
        ["id"],
        ["link_to_professions"],
    ])
    def test_content_in_detail(self, unexpected):
        result = (
            categories.models.CategoriesModel.objects.detail(2)
        )
        self.assertNotIn(unexpected, result[0])


class CategoriesViewTest(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = categories.models.CategoriesModel.objects.create(
            name="published category",
            is_published=True,
        )
        cls.category2 = categories.models.CategoriesModel.objects.create(
            name="unpublished category",
        )

    def test_all_categories(self):
        response = self.client.get(
            django.urls.reverse(
                "categories:all",
            ),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(len(response.data), 2)

    def test_published(self):
        response = self.client.get(
            django.urls.reverse(
                "categories:published",
            ),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(len(response.data), 1)

    def test_create_category(self):
        num_categories_initial = (
            categories.models.CategoriesModel.objects.all()
        ).count()
        response_create_category = self.client.post(
            django.urls.reverse(
                "categories:create_category",
            ),
            data={"name": "unpublished category 2"},
        )
        new_num_categories = (
            categories.models.CategoriesModel.objects.all()
        ).count()
        self.assertEqual(
            response_create_category.status_code,
            http.HTTPStatus.CREATED,
        )
        self.assertEqual(
            num_categories_initial + 1,
            new_num_categories,
        )
