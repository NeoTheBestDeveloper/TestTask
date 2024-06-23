from os import getenv

__all__ = [
    "UndefinedEnvError",
    "Env",
    "EnvList",
]


class UndefinedEnvError(Exception):
    """Исключение происходит, когда искомая переменная окружения не была передана."""

    def __init__(self, env_name: str) -> None:
        msg = f'Env name="{env_name}"'
        super().__init__(msg)


def Env[T](env_name: str, variable_type: type[T]) -> T:  # noqa: N802
    """Получение переменной окружения с приведением ее к переданном типу."""
    env = getenv(env_name, None)

    if env is None:
        raise UndefinedEnvError(env_name)

    return variable_type(env)


def EnvList[T](env_name: str, list_item_type: type[T]) -> list[T]:  # noqa: N802
    """Получение переменной окружения в виде списка с приведением ее элементом к переданном типу."""
    env = getenv(env_name, None)

    if env is None:
        raise UndefinedEnvError(env_name)

    return map(list_item_type, env.split())
