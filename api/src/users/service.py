from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Manager

__all__ = [
    "UserService",
]


class UserService:
    _manager: Manager = Token.objects

    def login(self, username: str, password: str) -> str | None:
        user = authenticate(username=username, password=password)
        if user:
            token, _ = self._manager.get_or_create(user=user)
            return token.key
        return None

    def logout(self, user: User) -> None:
        token = self._manager.get(user=user)
        token.delete()

    def is_token_valid(self, token: str) -> bool:
        return self._manager.filter(key=token).exists()

    def create(self, username: str, email: str, password: str) -> User:
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        return user
