from django.contrib.auth.models import User
from rest_framework.serializers import CharField, ModelSerializer

__all__ = [
    "UserSerializer",
]


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
