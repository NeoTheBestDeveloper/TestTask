from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Manager
from rest_framework.authtoken.models import Token

__all__ = [
    "UserService",
]


class UserService:
    """Класс для работы с пользователями."""

    _token_manager: Manager = Token.objects

    def login(self, username: str, password: str) -> str | None:
        """Проверка наличия пользователя в базе, а так же соответствие пароля.
        Если все ок, то вернем access токен, либо None.
        """
        user = authenticate(username=username, password=password)
        if user:
            token, _ = self._token_manager.get_or_create(user=user)
            return token.key
        return None

    def logout(self, user: User) -> None:
        """Удаление access токена из базы для переданного пользователя.
        Это завершит его сессию.
        """
        token = self._token_manager.get(user=user)
        token.delete()

    def is_token_valid(self, token: str) -> bool:
        """Проверка на наличие токена в базе."""
        return self._token_manager.filter(key=token).exists()

    def create(self, username: str, email: str, password: str) -> User:
        """Создание нового пользователя."""
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        return user
