from typing import ClassVar

from django.db.models import Manager, ObjectDoesNotExist

from api.models import EquipmentTypeModel
from api.dto import EquipmentType

__all__ = [
    "EquipmentTypeRepository",
]


class EquipmentTypeRepository:
    _manager: ClassVar[Manager] = EquipmentTypeModel.objects

    def fetch_by_id(self, equipment_type_id: int) -> EquipmentType | None:
        try:
            return self._manager.get(pk=equipment_type_id)
        except ObjectDoesNotExist:
            return None
