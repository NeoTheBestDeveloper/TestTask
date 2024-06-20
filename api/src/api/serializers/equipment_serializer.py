from rest_framework.serializers import CharField, IntegerField, Serializer

__all__ = [
    "EquipmentSerializer",
]


class EquipmentSerializer(Serializer):
    id = IntegerField(required=False)
    type_id = IntegerField(required=True)
    serial_number = CharField(required=True, max_length=255)
    description = CharField(required=True)
