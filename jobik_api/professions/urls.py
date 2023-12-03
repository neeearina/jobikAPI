import django.urls

import professions.views

urlpatterns = [
    django.urls.path(
        "all/",
        professions.views.AllProfessionsView.as_view({"get": "list"}),
    ),
]
