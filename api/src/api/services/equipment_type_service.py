from api.dto import EquipmentType
from api.repositories import EquipmentTypeRepository

__all__ = [
    "EquipmentTypeService",
]


class EquipmentTypeService:
    _repository = EquipmentTypeRepository()

    def filter_by(
        self,
        name: str | None = None,
        serial_number_mask: str | None = None,
        limit: int = 10,
        page: int = 1,
    ) -> list[EquipmentType]:
        return self._repository.filter_with_pagination(name, serial_number_mask, limit, page)
