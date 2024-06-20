from rest_framework.serializers import CharField, IntegerField, Serializer, ValidationError
from rest_framework.validators import UniqueValidator

from api.models import EquipmentModel, EquipmentTypeModel

__all__ = [
    "EquipmentSerializer",
]


class EquipmentSerializer(Serializer):
    id = IntegerField(required=False)
    type_id = IntegerField(required=True)
    serial_number = CharField(
        required=True,
        max_length=255,
        validators=[
            UniqueValidator(
                EquipmentModel.objects.filter(archived=False),
            ),
        ],
    )
    description = CharField(required=True)

    def validate_type_id(self, value: int) -> int:
        if not EquipmentTypeModel.objects.filter(pk=value).exists():
            msg = f"Equipment type with id={value} does not exists"
            raise ValidationError(msg)

        return value
