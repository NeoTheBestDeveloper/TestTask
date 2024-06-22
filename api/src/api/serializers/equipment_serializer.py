from typing import Mapping
from re import match
from django.db.models import ObjectDoesNotExist
from rest_framework.serializers import CharField, IntegerField, Serializer, ValidationError
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.validators import UniqueValidator

from api.models import EquipmentModel, EquipmentTypeModel

__all__ = [
    "EquipmentSerializer",
]


class EquipmentSerializer(Serializer):
    id = IntegerField(required=False)
    type_id = IntegerField(required=True)
    serial_number = CharField(required=True, max_length=255)
    description = CharField(required=True)

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=EquipmentModel.objects.filter(archived=False),
                fields=["serial_number", "type_id"],
            ),
        ]

    def _regexp_pattern_from_mask(self, mask: str) -> str:
        pattern = mask.replace("Z", r"[\-_@]")
        pattern = pattern.replace("N", r"\d")
        pattern = pattern.replace("A", "[A-Z]")
        pattern = pattern.replace("a", "[a-z]")
        return pattern.replace("X", "[A-Z0-9]")

    def validate(self, attrs: Mapping) -> Mapping:
        type_id = attrs["type_id"]
        serial_number = attrs["serial_number"]

        try:
            type_obj = EquipmentTypeModel.objects.get(pk=type_id)
        except ObjectDoesNotExist:
            msg = f"Equipment type with id={type_id} does not exists"
            raise ValidationError(msg)

        pattern = self._regexp_pattern_from_mask(type_obj.serial_number_mask)

        if not match(pattern, serial_number):
            msg = f"Serial number '{serial_number}' is not valid for mask '{type_obj.serial_number_mask}'"
            raise ValidationError(msg)

        return super().validate(attrs)
