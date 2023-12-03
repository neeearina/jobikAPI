import django.urls

import professions.views

urlpatterns = [
    django.urls.path(
        "all/",
        professions.views.AllProfessionsView.as_view({"get": "list"}),
    ),
    django.urls.path(
        "published/",
        professions.views.PublishedProfessionsView.as_view({"get": "list"}),
    ),
    django.urls.path(
        "detail/<int:pk>/",
        professions.views.ProfessionDetailView.as_view(),
    ),
]
