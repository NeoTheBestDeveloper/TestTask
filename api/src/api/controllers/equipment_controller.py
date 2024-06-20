from django.http import JsonResponse
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
    service: EquipmentService = EquipmentService()

    def get(self, _request: Request, pk: int) -> JsonResponse:
        equipment = self.service.fetch_by_id(pk)

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


class EquipmentControllerList(APIView):
    service: EquipmentService = EquipmentService()

    def get(self, _request: Request) -> JsonResponse:
        return JsonResponse(
            {
                "data": [],
                "detail": "",
            },
        )

    def post(self, request: Request) -> JsonResponse:
        serializer = EquipmentSerializer(data=request.data, many=True)

        if not serializer.is_valid():
            return JsonResponse(
                {
                    "data": serializer.errors,
                    "detail": "Invalid input data",
                },
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        created_equipments = []
        for item in serializer.validated_data:
            created_equipments.append(self.service.create(**item))

        serializer = EquipmentSerializer(created_equipments, many=True)

        return JsonResponse(
            {
                "data": serializer.data,
                "detail": "",
            }
        )
