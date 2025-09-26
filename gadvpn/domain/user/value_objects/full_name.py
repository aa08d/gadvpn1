from gadvpn.domain.common.value_objects import ValueObject


class FullName(ValueObject):
    def __init__(self, first_name: str, last_name: str | None) -> None:
        self._first_name = first_name
        self._last_name = last_name

    @property
    def value(self) -> str:
        return f"{self._first_name} {self._last_name}"

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name
