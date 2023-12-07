import django.urls
import drf_yasg
import drf_yasg.views
import rest_framework.permissions

schema_view = drf_yasg.views.get_schema_view(
    drf_yasg.openapi.Info(
        title="Джобик API",
        default_version="v1",
        description="Джобик - мобильное профориентационное "
                    "приложение для подростков",
        terms_of_service="https://www.google.com/policies/terms/",
        license=drf_yasg.openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(rest_framework.permissions.AllowAny,),
)

urlpatterns = [
    django.urls.path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    django.urls.path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    django.urls.path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
