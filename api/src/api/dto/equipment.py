from dataclasses import dataclass

__all__ = [
    "Equipment",
]


@dataclass(slots=True, frozen=True)
class Equipment:
    id: int
    type_name: str
    serial_number: str
    description: str
