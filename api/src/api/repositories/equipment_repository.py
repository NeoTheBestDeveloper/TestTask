from typing import ClassVar

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager

from api.models import EquipmentModel
from api.dto import Equipment

__all__ = [
    "EquipmentRepository",
]


class EquipmentRepository:
    _manager: ClassVar[Manager] = EquipmentModel.objects

    def soft_delete(self, equipment_id: int) -> None:
        self._manager.filter(pk=equipment_id, archived=False).update(archived=True)

    def fetch_by_id(self, equipment_id: int) -> None | Equipment:
        try:
            return self._manager.get(pk=equipment_id, archived=False)
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
