from django.db.models import PROTECT, CharField, ForeignKey, Model, TextField

__all__ = [
    "Equipment",
]


class Equipment(Model):
    title = CharField(verbose_name="Наименование", max_length=255, null=False)
    type = ForeignKey(
        verbose_name="Тип оборудования",
        to="EquipmentType",
        on_delete=PROTECT,
        null=False,
        related_name="equipments",
    )
    serial_number = CharField(verbose_name="Серийный номер", max_length=255, unique=True, null=False)
    description = TextField(verbose_name="Примечание", null=False, default="")

    class Meta:
        db_table = "equipments"
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудования"

    def __str__(self) -> str:
        return (
            f"Equipment(title={self.title}, type={self.type}, "
            f"serial_number={self.serial_number}, description={self.description})"
        )
