import django.contrib
import django.urls

app_name = "jobik_api"

urlpatterns = [
    django.urls.path(
        "admin/",
        django.contrib.admin.site.urls,
    ),
    django.urls.path(
        "api/categories/",
        django.urls.include("categories.urls"),
    ),
    django.urls.path(
        "api/professions/",
        django.urls.include("professions.urls"),
    ),
]
