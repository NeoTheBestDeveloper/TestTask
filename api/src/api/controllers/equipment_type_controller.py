from dataclasses import asdict

from django.conf import settings
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from api.services import EquipmentTypeService

__all__ = [
    "EquipmentTypeControllerList",
]


class EquipmentTypeControllerList(APIView):
    permission_classes = [IsAuthenticated]
    _service: EquipmentTypeService = EquipmentTypeService()

    def get(self, request: Request) -> JsonResponse:
        """Получение списка из типов оборудования с пагинацией и фильтрацией."""
        pages_count, equipment_types = self._service.filter_with_pagination(
            name=request.query_params.get("name"),
            serial_number_mask=request.query_params.get("serial_number_mask"),
            limit=request.query_params.get("limit") or settings.DEFAULT_PAGINATION_LIMIT,
            page=request.query_params.get("page") or settings.DEFAULT_PAGINATION_OFFSET,
        )

        return JsonResponse(
            {
                "data": {
                    "equipment_types": [asdict(item) for item in equipment_types],
                    "pages_count": pages_count,
                },
                "detail": "ok",
            },
        )
