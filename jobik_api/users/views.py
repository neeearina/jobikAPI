import django.contrib.auth
import rest_framework.authtoken.models
import rest_framework.response
import rest_framework.status
import rest_framework.views

import users.models
import users.serializers

__all__ = [
    "UserRegister",
    "UserLogin",
    "UserLogout",
]


class UserRegister(rest_framework.views.APIView):
    def post(self, request):
        serializer = users.serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return rest_framework.response.Response(
                serializer.data,
                status=rest_framework.status.HTTP_201_CREATED,
            )
        return rest_framework.response.Response(
            serializer.errors,
            status=rest_framework.status.HTTP_400_BAD_REQUEST,
        )


class UserLogin(rest_framework.views.APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = None
        if "@" in username:
            try:
                user = users.models.User.objects.get(email=username)
            except django.core.exceptions.ObjectDoesNotExist:
                pass
        if not user:
            user = django.contrib.auth.authenticate(
                username=username,
                password=password,
            )
        if user:
            token, _ = (
                rest_framework.authtoken.models.Token.objects
                .get_or_create(user=user)
            )
            return rest_framework.response.Response(
                {"token": token.key},
                status=rest_framework.status.HTTP_200_OK,
            )
        return rest_framework.response.Response(
            {"error": "Invalid credentials"},
            status=rest_framework.status.HTTP_401_UNAUTHORIZED,
        )


class UserLogout(rest_framework.views.APIView):
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return rest_framework.response.Response(
                {"message": "Successfully logged out."},
                status=rest_framework.status.HTTP_200_OK,
            )
        except Exception as e:
            return rest_framework.response.Response(
                {"error": str(e)},
                status=rest_framework.status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
