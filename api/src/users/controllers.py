from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from .serializers import UserSerializer

__all__ = [
    "UserRegistrationController",
    "UserLoginController",
]


class UserRegistrationController(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginController(APIView):
    def post(self, request: Request) -> JsonResponse:
        user = authenticate(username=request.data["username"], password=request.data["password"])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"data": token.key, "detail": "ok"})

        return JsonResponse({"data": "", "detail": "Invalid credentials"}, status=HTTP_401_UNAUTHORIZED)
