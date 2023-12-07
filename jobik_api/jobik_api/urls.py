import django.contrib
import django.urls

import jobik_api.yasg

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
    django.urls.path(
        "api/users/",
        django.urls.include("users.urls"),
    ),
]
urlpatterns += jobik_api.yasg.urlpatterns
