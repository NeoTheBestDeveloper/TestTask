from django.http import JsonResponse
from django.db import transaction
from rest_framework.request import Request
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.views import APIView

from api.serializers import EquipmentSerializer
from api.services import EquipmentService

__all__ = [
    "EquipmentController",
    "EquipmentControllerList",
]


class EquipmentController(APIView):
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

        serializer = EquipmentSerializer(instance=equipment)
        return JsonResponse(
            {
                "data": serializer.data,
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


class EquipmentControllerList(APIView):
    _service: EquipmentService = EquipmentService()

    def get(self, request: Request) -> JsonResponse:
        equipments = self._service.filter_by(
            equipment_type_id=request.query_params.get("type_id"),
            serial_number=request.query_params.get("serial_number"),
            description=request.query_params.get("description"),
            limit=request.query_params.get("limit") or 10,
            page=request.query_params.get("page") or 1,
        )

        serializer = EquipmentSerializer(equipments, many=True)

        return JsonResponse(
            {
                "data": serializer.data,
                "detail": "",
            },
        )

    @transaction.atomic
    def post(self, request: Request) -> JsonResponse:
        if not isinstance(request.data, list):
            return JsonResponse(
                {
                    "data": "",
                    "detail": "Expected JSON array",
                },
            )
        serializer = EquipmentSerializer(data=request.data, many=True)

        if not serializer.is_valid():
            return JsonResponse(
                {
                    "data": serializer.errors,
                    "detail": "Invalid input data",
                },
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        created_equipments = [self._service.create(**item) for item in serializer.validated_data]

        serializer = EquipmentSerializer(created_equipments, many=True)

        return JsonResponse(
            {
                "data": serializer.data,
                "detail": "",
            },
        )
