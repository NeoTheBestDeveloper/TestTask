from dataclasses import asdict
from typing import Final

from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from api.serializers import EquipmentSerializer, UpdateEquipmentSerializer
from api.services import EquipmentService

__all__ = [
    "EquipmentController",
    "EquipmentControllerList",
]

DEFAULT_PAGINATION_OFFSET: Final[int] = 1
DEFAULT_PAGINATION_LIMIT: Final[int] = 10


class EquipmentController(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    _service: EquipmentService = EquipmentService()

    def get(self, _request: Request, pk: int) -> JsonResponse:
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
                "detail": "",
            },
        )

    def delete(self, _request: Request, pk: int) -> JsonResponse:
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
        equipment = self._service.fetch_by_id(pk)

        if equipment is None:
            return JsonResponse(
                {
                    "data": "",
                    "detail": "Entity not found",
                },
                status=HTTP_404_NOT_FOUND,
            )

        serializer = UpdateEquipmentSerializer(data=request.data, context={"id": pk})
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    _service: EquipmentService = EquipmentService()

    def get(self, request: Request) -> JsonResponse:
        equipments = self._service.filter_by(
            equipment_type_id=request.query_params.get("type_id"),
            serial_number=request.query_params.get("serial_number"),
            description=request.query_params.get("description"),
            limit=request.query_params.get("limit") or DEFAULT_PAGINATION_LIMIT,
            page=request.query_params.get("page") or DEFAULT_PAGINATION_OFFSET,
        )

        return JsonResponse(
            {
                "data": [asdict(item) for item in equipments],
                "detail": "",
            },
        )

    def post(self, request: Request) -> JsonResponse:
        if not isinstance(request.data, list):
            return JsonResponse(
                {
                    "data": "",
                    "detail": "Expected JSON array",
                },
            )

        validated_data = []
        unprocessed_data = []

        for item in request.data:
            serializer = EquipmentSerializer(data=item)

            if not serializer.is_valid():
                unprocessed_data.append(
                    {
                        "data": serializer.data,
                        "detail": serializer.errors,
                    }
                )
            else:
                validated_data.append(serializer.validated_data)

        created_equipments = [self._service.create(**item) for item in validated_data]

        if not unprocessed_data:
            return JsonResponse(
                {
                    "data": [asdict(item) for item in created_equipments],
                    "detail": "",
                },
            )

        return JsonResponse(
            {
                "data": [asdict(item) for item in created_equipments],
                "detail": unprocessed_data,
            },
            status=HTTP_422_UNPROCESSABLE_ENTITY,
        )
