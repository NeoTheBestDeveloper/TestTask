from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from .serializers import UserSerializer

__all__ = [
    "UserRegistrationController",
    "UserLoginController",
    "UserLogoutController",
    "FetchMeController",
]


class UserRegistrationController(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginController(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> JsonResponse:
        user = authenticate(username=request.data["username"], password=request.data["password"])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"data": token.key, "detail": "ok"})

        return JsonResponse({"data": "", "detail": "Invalid credentials"}, status=HTTP_401_UNAUTHORIZED)


class FetchMeController(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> JsonResponse:
        serializer = UserSerializer(request.user)
        return JsonResponse(
            {
                "data": serializer.data,
                "detail": "ok",
            }
        )


class UserLogoutController(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> JsonResponse:
        token = Token.objects.get(user=request.user)
        token.delete()
        return JsonResponse({"data": "", "detail": "ok"})
