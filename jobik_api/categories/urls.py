import django.urls

import categories.views

app_name = "categories"
urlpatterns = [
    django.urls.path(
        "published/",
        categories.views.PublishedCategoriesView.as_view({"get": "list"}),
    ),
]
