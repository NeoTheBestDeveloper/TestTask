from django.db.models import CharField, Model

__all__ = [
    "EquipmentType",
]


class EquipmentType(Model):
    name = CharField(verbose_name="Наименование типа", max_length=255, null=False)
    serial_number_mask = CharField(verbose_name="Маска серийного номера", max_length=255, null=False)

    class Meta:
        db_table = "equipment_types"
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"

    def __str__(self) -> str:
        return f"EquipmentType(name={self.name}, mask={self.serial_number_mask})"
