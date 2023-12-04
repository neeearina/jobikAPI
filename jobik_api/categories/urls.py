import django.urls

import categories.views

app_name = "categories"

urlpatterns = [
    django.urls.path(
        "all/",
        categories.views.AllCategoriesView.as_view({"get": "list"}),
        name="all_categories",
    ),
    django.urls.path(
        "published/",
        categories.views.PublishedCategoriesView.as_view({"get": "list"}),
        name="published",
    ),
    django.urls.path(
        "create/",
        categories.views.CreateCategoryView.as_view(),
        name="create_category",
    ),
    django.urls.path(
        "detail/<int:pk>/",
        categories.views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]
