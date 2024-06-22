from typing import ClassVar

from django.core.paginator import EmptyPage, Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager

from api.models import EquipmentModel, EquipmentTypeModel
from api.dto import Equipment

__all__ = [
    "EquipmentRepository",
]


class EquipmentRepository:
    _manager: ClassVar[Manager] = EquipmentModel.objects
    _equipment_type_manager: ClassVar[Manager] = EquipmentTypeModel.objects

    def filter_with_pagination(
        self,
        serial_number: str | None = None,
        description: str | None = None,
        limit: int = 10,
        page: int = 1,
    ) -> tuple[int, list[Equipment]]:
        filter_settings = {
            "archived": False,
        }

        if serial_number is not None:
            filter_settings["serial_number"] = serial_number

        if description is not None:
            filter_settings["description__icontains"] = description

        query_set = (
            self._manager.defer("archived", "type_id", "type__serial_number_mask", "type__id")
            .filter(**filter_settings)
            .select_related("type")
        )
        paginator = Paginator(
            query_set,
            per_page=limit,
        )

        try:
            result = paginator.page(page)
            return paginator.num_pages, [
                Equipment(
                    id=item.id,
                    type_name=item.type.name,
                    serial_number=item.serial_number,
                    description=item.description,
                )
                for item in result
            ]

        except EmptyPage:
            return paginator.num_pages, []

    def soft_delete(self, equipment_id: int) -> None:
        self._manager.filter(pk=equipment_id, archived=False).update(archived=True)

    def fetch_by_id(self, equipment_id: int) -> None | Equipment:
        result = (
            self._manager.defer("archived", "type__serial_number_mask")
            .select_related("type")
            .filter(pk=equipment_id, archived=False)
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
        model = EquipmentModel(type_id=type_id, serial_number=serial_number, description=description)
        model.save()

        return Equipment(
            model.id,
            model.type.name,
            model.serial_number,
            model.description,
        )

    def update(self, id: int, serial_number: str, description: str, type_id: int) -> Equipment:
        self._manager.filter(pk=id).update(serial_number=serial_number, description=description, type_id=type_id)
        new_type = self._equipment_type_manager.filter(pk=type_id).only("name").first()
        return Equipment(id, new_type.name, serial_number, description)
