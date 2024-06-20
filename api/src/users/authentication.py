from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request

__all__ = [
    "CustomTokenAuthentication",
]


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request: Request):
        if request.META.get("HTTP_AUTHORIZATION"):
            request.META["HTTP_AUTHORIZATION"] = request.META["HTTP_AUTHORIZATION"].replace("Bearer", "Token")
        return super().authenticate(request)
