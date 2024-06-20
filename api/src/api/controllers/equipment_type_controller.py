from dataclasses import asdict

from django.http import JsonResponse
from django.conf import settings
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.services import EquipmentTypeService


class EquipmentTypeControllerList(APIView):
    permission_classes = [IsAuthenticated]
    _service: EquipmentTypeService = EquipmentTypeService()

    def get(self, request: Request) -> JsonResponse:
        equipment_types = self._service.filter_by(
            name=request.query_params.get("name"),
            serial_number_mask=request.query_params.get("serial_number_mask"),
            limit=request.query_params.get("limit") or settings.DEFAULT_PAGINATION_LIMIT,
            page=request.query_params.get("page") or settings.DEFAULT_PAGINATION_OFFSET,
        )

        return JsonResponse(
            {
                "data": [asdict(i) for i in equipment_types],
                "detail": "ok",
            },
        )
