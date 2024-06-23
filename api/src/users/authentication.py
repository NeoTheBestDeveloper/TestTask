from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request

__all__ = [
    "CustomTokenAuthentication",
]


class CustomTokenAuthentication(TokenAuthentication):
    """Класс для аунтефикации пользователя. Обычно пишут перед токеном Bearer, но DRF пишет в заголовок Token.
    Данный класс исправляет данную фичу DRF, позволяя писать токен в HTTP загловке после слова Bearer.
    """

    def authenticate(self, request: Request):
        """Замена Bearer на Token, чтобы DRF смог проверить токен."""
        if request.META.get("HTTP_AUTHORIZATION"):
            request.META["HTTP_AUTHORIZATION"] = request.META["HTTP_AUTHORIZATION"].replace("Bearer", "Token")
        return super().authenticate(request)
