from re import match


__all__ = [
    "is_serial_number_valid",
]


def is_serial_number_valid(serial_number: str, mask: str) -> bool:
    """Проверка на валидность серийного номера по указанной маске."""
    pattern = mask.replace("Z", r"[\-_@]")
    pattern = pattern.replace("N", r"\d")
    pattern = pattern.replace("A", "[A-Z]")
    pattern = pattern.replace("a", "[a-z]")
    pattern = f"^{pattern.replace("X", "[A-Z0-9]")}$"

    return bool(match(pattern, serial_number))
