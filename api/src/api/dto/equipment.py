from dataclasses import dataclass

__all__ = [
    "Equipment",
]


@dataclass(slots=True, frozen=True)
class Equipment:
    id: int
    type_id: int
    serial_number: str
    description: str
