from typing import ClassVar


class AppError(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An app error occurred"
