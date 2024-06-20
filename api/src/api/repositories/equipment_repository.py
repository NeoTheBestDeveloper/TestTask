from typing import ClassVar

from django.core.paginator import EmptyPage, Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager

from api.models import EquipmentModel
from api.dto import Equipment

__all__ = [
    "EquipmentRepository",
]


class EquipmentRepository:
    _manager: ClassVar[Manager] = EquipmentModel.objects

    def filter_with_pagination(
        self,
        equipment_type_id: int | None = None,
        serial_number: str | None = None,
        description: str | None = None,
        limit: int = 10,
        page: int = 1,
    ) -> list[Equipment]:
        filter_settings = {
            "archived": False,
        }

        if equipment_type_id is not None:
            filter_settings["type_id"] = equipment_type_id

        if serial_number is not None:
            filter_settings["serial_number"] = serial_number

        if description is not None:
            filter_settings["description"] = description

        paginator = Paginator(self._manager.defer("archived").filter(**filter_settings), per_page=limit)

        try:
            result = paginator.page(page)
            return [
                Equipment(
                    id=item.id,
                    type_id=item.type_id,
                    serial_number=item.serial_number,
                    description=item.description,
                )
                for item in result
            ]

        except EmptyPage:
            return []

    def soft_delete(self, equipment_id: int) -> None:
        self._manager.filter(pk=equipment_id, archived=False).update(archived=True)

    def fetch_by_id(self, equipment_id: int) -> None | Equipment:
        try:
            result = self._manager.get(pk=equipment_id, archived=False)
            return Equipment(
                id=result.id,
                type_id=result.type_id,
                serial_number=result.serial_number,
                description=result.description,
            )
        except ObjectDoesNotExist:
            return None

    def create(self, type_id: int, serial_number: str, description: str) -> Equipment:
        model = EquipmentModel(type_id=type_id, serial_number=serial_number, description=description)
        model.save()

        return Equipment(
            model.id,
            model.type_id,
            model.serial_number,
            model.description,
        )

    def update(self, id: int, serial_number: str, description: str, type_id: int) -> Equipment:
        self._manager.filter(pk=id).update(serial_number=serial_number, description=description, type_id=type_id)
        return Equipment(id, type_id, serial_number, description)
