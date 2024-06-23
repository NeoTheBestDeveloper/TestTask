from typing import ClassVar

from api.dto import Equipment
from api.repositories import EquipmentRepository

__all__ = [
    "EquipmentService",
]


class EquipmentService:
    """Сервис для взаимодействия с оборудованием."""

    _repository: ClassVar[EquipmentRepository] = EquipmentRepository()

    def soft_delete(self, pk: int) -> None:
        """Помечает указанное оборудование как удаленное, реального удаления из базы не происходит."""
        self._repository.soft_delete(pk)

    def fetch_by_id(self, pk: int) -> Equipment | None:
        """Поиск оборудования по id, вернет None, если не сможет найти."""
        return self._repository.fetch_by_id(pk)

    def filter_with_pagination(
        self,
        serial_number: str | None = None,
        description: str | None = None,
        limit: int = 10,
        page: int = 1,
    ) -> tuple[int, list[Equipment]]:
        """Поиск оборудования по заданным параметрам с пагинацией.
        Вернет котреж, где первый элемент - это число страниц в пагинации, а второй - это сама страница из оборудования.
        """
        return self._repository.filter_with_pagination(serial_number, description, limit, page)

    def create(self, type_id: int, serial_number: str, description: str) -> Equipment:
        """Создание оборудования с указанными свойствами."""
        return self._repository.create(type_id, serial_number, description)

    def update(self, pk: int, serial_number: str, description: str, type_id: int) -> Equipment:
        """Обновит поля serial_number, description, type_id у оборудования с указанным pk."""
        return self._repository.update(pk, serial_number, description, type_id)
