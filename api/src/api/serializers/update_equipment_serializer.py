from typing import Mapping
from rest_framework.serializers import CharField, IntegerField, Serializer, ValidationError

from api.models import EquipmentModel, EquipmentTypeModel

__all__ = [
    "UpdateEquipmentSerializer",
]


class UpdateEquipmentSerializer(Serializer):
    type_id = IntegerField(required=True)
    serial_number = CharField(
        required=True,
        max_length=255,
    )
    description = CharField(required=True)

    def validate(self, attrs: Mapping) -> Mapping:
        type_id = attrs["type_id"]
        pk = self.context["id"]
        serial_number = attrs["serial_number"]

        if not EquipmentTypeModel.objects.filter(pk=type_id).exists():
            msg = f"Equipment type with id={type_id} does not exists"
            raise ValidationError(msg)

        if EquipmentModel.objects.filter(serial_number=serial_number, archived=False).exclude(pk=pk):
            msg = "Bla bla"
            raise ValidationError(msg, code="unique")

        return super().validate(attrs)
