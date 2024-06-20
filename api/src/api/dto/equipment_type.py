from dataclasses import dataclass

__all__ = [
    "EquipmentType",
]


@dataclass(slots=True, frozen=True)
class EquipmentType:
    id: int
    name: str
    serial_number_mask: str
