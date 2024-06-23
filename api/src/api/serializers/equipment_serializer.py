from collections.abc import Mapping

from django.db.models import ObjectDoesNotExist
from rest_framework.serializers import CharField, IntegerField, Serializer, ValidationError
from rest_framework.validators import UniqueTogetherValidator

from api.models import EquipmentModel, EquipmentTypeModel
from api.utils import is_serial_number_valid

__all__ = [
    "EquipmentSerializer",
]


class EquipmentSerializer(Serializer):
    """Сериализатор для валидации данных оборудования."""

    id = IntegerField(required=False)
    type_id = IntegerField(required=True)
    serial_number = CharField(required=True, max_length=255)
    description = CharField(required=True)

    class Meta:
        validators = [  # noqa: RUF012
            UniqueTogetherValidator(
                queryset=EquipmentModel.objects.filter(archived=False),
                fields=["serial_number", "type_id"],
                message="Серийный номер должен быть уникальным.",
            ),
        ]

    def validate(self, attrs: Mapping) -> Mapping:
        """Валидация полей. Проверка на существования типа оборудования из type_id и корректности серийного номера."""
        type_id = attrs["type_id"]
        serial_number = attrs["serial_number"]

        try:
            type_obj = EquipmentTypeModel.objects.get(pk=type_id)
        except ObjectDoesNotExist:
            msg = f"Equipment type with id={type_id} does not exists"
            raise ValidationError(msg)  # noqa: B904

        if not is_serial_number_valid(serial_number, type_obj.serial_number_mask):
            msg = f"Серийный номер '{serial_number}' не подходит для маски '{type_obj.serial_number_mask}'"
            raise ValidationError(msg)

        return super().validate(attrs)
