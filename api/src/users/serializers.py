from django.contrib.auth.models import User
from rest_framework.serializers import CharField, Serializer
from rest_framework.validators import UniqueValidator

__all__ = [
    "UserLoginSerializer",
    "UserCreateSerializer",
]


class UserLoginSerializer(Serializer):
    username = CharField(max_length=255, required=True)
    password = CharField(max_length=255, required=True)


class UserCreateSerializer(Serializer):
    username = CharField(
        max_length=150,
        required=True,
        validators=[UniqueValidator(User.objects.all(), message="Пользователь с таким логином уже существует")],
    )
    email = CharField(max_length=254, required=True)
    password = CharField(max_length=255, required=True)
