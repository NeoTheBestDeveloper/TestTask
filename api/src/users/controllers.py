from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.views import APIView

from .serializers import UserCreateSerializer, UserLoginSerializer
from .service import UserService

__all__ = [
    "UserRegistrationController",
    "UserLoginController",
    "UserLogoutController",
    "CheckTokenController",
]


class UserRegistrationController(CreateAPIView):
    permission_classes = [AllowAny]
    _service: UserService = UserService()

    def post(self, request: Request) -> JsonResponse:
        serializer = UserCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(
                {"data": serializer.errors, "detail": "Неверный формат данных"},
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        user = self._service.create(**serializer.validated_data)

        return JsonResponse({"data": {**serializer.validated_data, "id": user.id}, "detail": "ok"})


class UserLoginController(APIView):
    permission_classes = [AllowAny]
    _service: UserService = UserService()

    def post(self, request: Request) -> JsonResponse:
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(
                {"data": serializer.errors, "detail": "Неверный формат данных"},
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        token = self._service.login(**serializer.validated_data)

        if token is None:
            return JsonResponse({"data": "", "detail": "Неверный пароль или логин."}, status=HTTP_401_UNAUTHORIZED)
        return JsonResponse({"data": token, "detail": "ok"})


class CheckTokenController(APIView):
    permission_classes = [AllowAny]
    _service: UserService = UserService()

    def post(self, request: Request) -> JsonResponse:
        token = request.data.get("token")

        if token is None:
            return JsonResponse(
                {"data": "Поле 'token' обязательно", "detail": "Неверный формат данных"},
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        return JsonResponse(
            {
                "data": self._service.is_token_valid(token),
                "detail": "ok",
            },
        )


class UserLogoutController(APIView):
    permission_classes = [IsAuthenticated]
    _service: UserService = UserService()

    def post(self, request: Request) -> JsonResponse:
        self._service.logout(request.user)
        return JsonResponse({"data": "", "detail": "ok"})
