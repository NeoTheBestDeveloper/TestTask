from api.dto import EquipmentType
from api.repositories import EquipmentTypeRepository

__all__ = [
    "EquipmentTypeService",
]


class EquipmentTypeService:
    """Сервис для взаимодействия с типами оборудования."""

    _repository = EquipmentTypeRepository()

    def filter_with_pagination(
        self,
        name: str | None = None,
        serial_number_mask: str | None = None,
        limit: int = 10,
        page: int = 1,
    ) -> tuple[int, list[EquipmentType]]:
        """Поиск типов оборудования по заданным параметрам с пагинацией.
        Вернет котреж, где первый элемент - это число страниц в пагинации,
        а второй - это сама страница из типов оборудования.
        """
        return self._repository.filter_with_pagination(name, serial_number_mask, limit, page)
