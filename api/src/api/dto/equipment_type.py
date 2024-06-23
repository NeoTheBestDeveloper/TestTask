from dataclasses import dataclass

__all__ = [
    "EquipmentType",
]


@dataclass(slots=True, frozen=True)
class EquipmentType:
    """Представление типа оборудования в бизнес логике."""

    id: int
    name: str
    serial_number_mask: str
