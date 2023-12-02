from django.contrib import admin
from django.urls import path

import professions.views

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "api/categories/",
        professions.views.PublishedCategoriesView.as_view({"get": "list"}),
    ),
]
