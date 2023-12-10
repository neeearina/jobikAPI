import rest_framework.serializers

import users.models

__all__ = ["UserSerializer"]


class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = users.models.User(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
