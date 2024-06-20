from typing import ClassVar, NoReturn

from api.dto import Equipment
from api.repositories import EquipmentRepository, EquipmentTypeRepository


__all__ = [
    "EquipmentService",
]


class EquipmentService:
    _repository: ClassVar[EquipmentRepository] = EquipmentRepository()
    _equipment_type_repository: ClassVar[EquipmentTypeRepository] = EquipmentTypeRepository()

    def soft_delete(self, equipment_id: int) -> None:
        self._repository.soft_delete(equipment_id)

    def fetch_by_id(self, equipment_id: int) -> Equipment | None:
        return self._repository.fetch_by_id(equipment_id)

    def filter_by(
        self,
        equipment_type_id: int | None = None,
        serial_number: str | None = None,
        description: str | None = None,
        limit: int = 10,
        offset: int = 0,
    ) -> list[Equipment]: ...

    def create(self, type_id: int, serial_number: str, description: str) -> Equipment | NoReturn:
        equipment_type = self._equipment_type_repository.fetch_by_id(type_id)

        if equipment_type is None:
            raise RuntimeError("Invalid type id")

        return self._repository.create(type_id, serial_number, description)
