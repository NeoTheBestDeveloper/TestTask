from django.contrib.auth.models import User
from rest_framework.serializers import CharField, EmailField, Serializer
from rest_framework.validators import UniqueValidator

__all__ = [
    "UserLoginSerializer",
    "UserCreateSerializer",
]


class UserLoginSerializer(Serializer):
    """Сериализатор для валидации данных, которые требуются для входа в аккаунт."""

    username = CharField(max_length=150, min_length=3, required=True)
    password = CharField(max_length=255, min_length=8, required=True)


class UserCreateSerializer(Serializer):
    """Сериализатор для валидации данных, которые требуются для создания аккаунта."""

    username = CharField(
        max_length=150,
        min_length=3,
        required=True,
        validators=[UniqueValidator(User.objects.all(), message="Пользователь с таким логином уже существует")],
    )
    email = EmailField(max_length=254, required=True)
    password = CharField(max_length=255, min_length=8, required=True)
