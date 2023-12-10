import django.urls

import users.views

urlpatterns = [
    django.urls.path(
        "register/",
        users.views.UserRegister.as_view(),
        name="register",
    ),
    django.urls.path(
        "login/",
        users.views.UserLogin.as_view(),
        name="login",
    ),
    django.urls.path(
        "logout/",
        users.views.UserLogout.as_view(),
        name="logout",
    ),
]
