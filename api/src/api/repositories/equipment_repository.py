from typing import ClassVar

from django.core.paginator import EmptyPage, Paginator
from django.db.models import Manager

from api.dto import Equipment
from api.models import EquipmentModel, EquipmentTypeModel

__all__ = [
    "EquipmentRepository",
]


class EquipmentRepository:
    """Репозиторий для сущности Equipment.
    Инкапсулирует в себе логику работы с базой данных.
    """

    _equipment_manager: ClassVar[Manager] = EquipmentModel.objects
    _equipment_type_manager: ClassVar[Manager] = EquipmentTypeModel.objects

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
        filter_settings = {
            "archived": False,
        }

        if serial_number is not None:
            filter_settings["serial_number"] = serial_number

        if description is not None:
            filter_settings["description__icontains"] = description

        query_set = (
            self._equipment_manager.defer("archived", "type_id", "type__serial_number_mask", "type__id")
            .filter(**filter_settings)
            .select_related("type")
        )
        paginator = Paginator(
            query_set,
            per_page=limit,
        )

        try:
            result = paginator.page(page)
            equipments = [
                Equipment(
                    id=item.id,
                    type_name=item.type.name,
                    serial_number=item.serial_number,
                    description=item.description,
                )
                for item in result
            ]

            if equipments:
                return paginator.num_pages, equipments
            return 0, equipments

        except EmptyPage:
            return 0, []

    def soft_delete(self, pk: int) -> None:
        """Помечает указанное оборудование как удаленное, реального удаления из базы не происходит."""
        self._equipment_manager.filter(pk=pk, archived=False).update(archived=True)

    def fetch_by_id(self, pk: int) -> None | Equipment:
        """Поиск оборудования по id, вернет None, если не сможет найти."""
        result = (
            self._equipment_manager.defer("archived", "type__serial_number_mask")
            .select_related("type")
            .filter(pk=pk, archived=False)
            .first()
        )

        if result is None:
            return None

        return Equipment(
            id=result.id,
            type_name=result.type.name,
            serial_number=result.serial_number,
            description=result.description,
        )

    def create(self, type_id: int, serial_number: str, description: str) -> Equipment:
        """Создание оборудования с указанными свойствами."""
        model = EquipmentModel(type_id=type_id, serial_number=serial_number, description=description)
        model.save()

        return Equipment(
            model.id,
            model.type.name,
            model.serial_number,
            model.description,
        )

    def update(self, pk: int, serial_number: str, description: str, type_id: int) -> Equipment:
        """Обновит поля serial_number, description, type_id у оборудования с указанным pk."""
        self._manager.filter(pk=pk).update(serial_number=serial_number, description=description, type_id=type_id)
        new_type = self._equipment_type_manager.filter(pk=type_id).only("name").first()
        return Equipment(pk, new_type.name, serial_number, description)
