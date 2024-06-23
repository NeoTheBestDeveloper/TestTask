from dataclasses import asdict

from django.conf import settings
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.views import APIView

from api.services import EquipmentService
from api.serializers import EquipmentSerializer, UpdateEquipmentSerializer

__all__ = [
    "EquipmentController",
    "EquipmentControllerList",
]


class EquipmentController(APIView):
    permission_classes = [IsAuthenticated]
    _service: EquipmentService = EquipmentService()

    def get(self, _: Request, pk: int) -> JsonResponse:
        """Поиск конктретного оборудования по его id."""
        equipment = self._service.fetch_by_id(pk)

        if equipment is None:
            return JsonResponse(
                {
                    "data": {},
                    "detail": "Entity not found",
                },
                status=HTTP_404_NOT_FOUND,
            )

        return JsonResponse(
            {
                "data": asdict(equipment),
                "detail": "ok",
            },
        )

    def delete(self, _request: Request, pk: int) -> JsonResponse:
        """Удаление оборудования по его id."""
        equipment = self._service.fetch_by_id(pk)

        if equipment is None:
            return JsonResponse(
                {
                    "data": "",
                    "detail": "Entity not found",
                },
                status=HTTP_404_NOT_FOUND,
            )

        self._service.soft_delete(equipment.id)

        return JsonResponse({"data": "", "detail": "ok"})

    def put(self, request: Request, pk: int) -> JsonResponse:
        """Редактирование полей оборудования с указанным id."""
        equipment = self._service.fetch_by_id(pk)

        if equipment is None:
            return JsonResponse(
                {
                    "data": "",
                    "detail": "Entity not found",
                },
                status=HTTP_404_NOT_FOUND,
            )

        serializer = UpdateEquipmentSerializer(data=request.data, context={"old_equipment": equipment})
        if not serializer.is_valid():
            return JsonResponse(
                {
                    "data": serializer.errors,
                    "detail": "Invalid input data",
                },
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        new_equipment = self._service.update(id=pk, **serializer.validated_data)

        return JsonResponse(
            {
                "data": asdict(new_equipment),
                "detail": "ok",
            },
        )


class EquipmentControllerList(APIView):
    permission_classes = [IsAuthenticated]
    _service: EquipmentService = EquipmentService()

    def get(self, request: Request) -> JsonResponse:
        """Получение списка оборудования с фильтрацией и пагинацией."""
        pages_count, equipments = self._service.filter_by(
            serial_number=request.query_params.get("serial_number"),
            description=request.query_params.get("description"),
            limit=request.query_params.get("limit") or settings.DEFAULT_PAGINATION_LIMIT,
            page=request.query_params.get("page") or settings.DEFAULT_PAGINATION_OFFSET,
        )

        return JsonResponse(
            {
                "data": {
                    "equipments": [asdict(item) for item in equipments],
                    "pages_count": pages_count,
                },
                "detail": "ok",
            },
        )

    def post(self, request: Request) -> JsonResponse:
        """Создание одного или несколько записей с оборудованием, если часть записей будет некорректной,
        то корретные данные будут сохранены, а некорректные вернуться пользователю с указанием ошибок.
        """
        if not isinstance(request.data, list):
            return JsonResponse(
                {
                    "data": "",
                    "detail": "Expected JSON array",
                },
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        validated_data = []
        unprocessed_data = []

        for item in request.data:
            serializer = EquipmentSerializer(data=item)

            if not serializer.is_valid():
                unprocessed_data.append({"data": serializer.data, "detail": serializer.errors})
            else:
                validated_data.append(serializer.validated_data)

        created_equipments = [self._service.create(**item) for item in validated_data]

        if not unprocessed_data:
            return JsonResponse(
                {
                    "data": [asdict(item) for item in created_equipments],
                    "detail": "ok",
                },
            )

        return JsonResponse(
            {
                "data": [asdict(item) for item in created_equipments],
                "detail": unprocessed_data,
            },
            status=HTTP_422_UNPROCESSABLE_ENTITY,
        )
