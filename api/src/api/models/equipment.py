from django.db.models import PROTECT, BooleanField, CharField, ForeignKey, Model, TextField

__all__ = [
    "EquipmentModel",
]


class EquipmentModel(Model):
    type = ForeignKey(
        verbose_name="Тип оборудования",
        to="EquipmentTypeModel",
        on_delete=PROTECT,
        null=False,
        related_name="equipments",
    )
    serial_number = CharField(verbose_name="Серийный номер", max_length=255, unique=True, null=False)
    description = TextField(verbose_name="Примечание", null=False, default="")
    archived = BooleanField(verbose_name="", default=False)

    class Meta:
        db_table = "equipments"
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудования"

    def __str__(self) -> str:
        return f"Equipment(type={self.type}, serial_number={self.serial_number}, description={self.description})"
