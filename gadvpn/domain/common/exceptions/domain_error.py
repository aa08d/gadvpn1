from .app_error import AppError

class DomainError(AppError):
    @property
    def title(self) -> str:
        return "A domain error occurred"
