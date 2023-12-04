import django.urls

import professions.views

urlpatterns = [
    django.urls.path(
        "all/",
        professions.views.AllProfessionsView.as_view({"get": "list"}),
        name="all_professions",
    ),
    django.urls.path(
        "published/",
        professions.views.PublishedProfessionsView.as_view({"get": "list"}),
        name="published",
    ),
    django.urls.path(
        "detail/<int:pk>/",
        professions.views.ProfessionDetailView.as_view(),
        name="profession_detail",
    ),
    django.urls.path(
        "create/",
        professions.views.CreateProfessionView.as_view(),
        name="create_profession",
    ),
]
