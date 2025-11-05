from typing import Any
from fastapi import HTTPException, status


class APIException(HTTPException):
    def __init__(
        self,
        *,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        message: str = "Internal server error",
        code: str = "internal_server_error",
        details: Any | None = None,
        headers: dict | None = None,
    ):
        self.code = code
        self.message = message
        self.details = details
        super().__init__(status_code=status_code, detail=message, headers=headers)

    def to_dict(self) -> dict:
        data = {
            "code": self.code,
            "message": self.message,
            "status_code": self.status_code,
        }
        if self.details:
            data["details"] = self.details
        return data


class RouteNotFoundException(APIException):
    def __init__(self, route: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Route '{route}' not found",
            code="route_not_found",
        )


class ValidationModelException(APIException):
    def __init__(self, details: Any | None):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            message="Validation error",
            code="validation_error",
            details=details,
        )
