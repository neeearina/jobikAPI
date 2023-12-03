from django.contrib import admin
from django.urls import path

import categories.views

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "api/categories/",
        categories.views.PublishedCategoriesView.as_view({"get": "list"}),
    ),
]
