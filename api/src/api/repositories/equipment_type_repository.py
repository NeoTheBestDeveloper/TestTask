from typing import ClassVar

from django.db.models import Manager, ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage

from api.models import EquipmentTypeModel
from api.dto import EquipmentType

__all__ = [
    "EquipmentTypeRepository",
]


class EquipmentTypeRepository:
    _manager: ClassVar[Manager] = EquipmentTypeModel.objects

    def fetch_by_id(self, pk: int) -> EquipmentType | None:
        try:
            return self._manager.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def filter_with_pagination(
        self,
        name: str | None = None,
        serial_number_mask: str | None = None,
        limit: int = 10,
        page: int = 1,
    ) -> list[EquipmentType]:
        filter_settings = {}

        if name is not None:
            filter_settings["name"] = name

        if serial_number_mask is not None:
            filter_settings["serial_number_mask"] = serial_number_mask

        paginator = Paginator(self._manager.filter(**filter_settings), per_page=limit)

        try:
            result = paginator.page(page)
            return [
                EquipmentType(
                    id=item.id,
                    name=item.name,
                    serial_number_mask=item.serial_number_mask,
                )
                for item in result
            ]

        except EmptyPage:
            return []
