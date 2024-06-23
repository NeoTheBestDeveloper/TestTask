from typing import ClassVar

from django.core.paginator import EmptyPage, Paginator
from django.db.models import Manager, ObjectDoesNotExist

from api.dto import EquipmentType
from api.models import EquipmentTypeModel

__all__ = [
    "EquipmentTypeRepository",
]


class EquipmentTypeRepository:
    _type_manager: ClassVar[Manager] = EquipmentTypeModel.objects

    def fetch_by_id(self, pk: int) -> EquipmentType | None:
        """Поиск типа оборудования по pk, вернет None, если не сможет найти."""
        try:
            return self._type_manager.get(pk=pk)
        except ObjectDoesNotExist:
            return None

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
        filter_settings = {}

        if name is not None:
            filter_settings["name"] = name

        if serial_number_mask is not None:
            filter_settings["serial_number_mask"] = serial_number_mask

        paginator = Paginator(self._type_manager.filter(**filter_settings), per_page=limit)

        try:
            result = paginator.page(page)
            types = [
                EquipmentType(
                    id=item.id,
                    name=item.name,
                    serial_number_mask=item.serial_number_mask,
                )
                for item in result
            ]
            if types:
                return paginator.num_pages, types
            return 0, types

        except EmptyPage:
            return 0, []
