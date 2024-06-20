from dataclasses import asdict
from typing import Final

from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.services import EquipmentTypeService

DEFAULT_PAGINATION_OFFSET: Final[int] = 1
DEFAULT_PAGINATION_LIMIT: Final[int] = 10


class EquipmentTypeControllerList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    _service: EquipmentTypeService = EquipmentTypeService()

    def get(self, request: Request) -> JsonResponse:
        equipment_types = self._service.filter_by(
            name=request.query_params.get("name"),
            serial_number_mask=request.query_params.get("serial_number_mask"),
            limit=request.query_params.get("limit") or DEFAULT_PAGINATION_LIMIT,
            page=request.query_params.get("page") or DEFAULT_PAGINATION_OFFSET,
        )

        return JsonResponse(
            {
                "data": [asdict(i) for i in equipment_types],
                "detail": "",
            },
        )
