from common.exceptions.api import APIException, status


class ServiceNotFoundException(APIException):
    def __init__(self, service_name: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Service '{service_name}' not found",
            code="service_not_found",
        )


class ServiceUnavailableException(APIException):
    def __init__(self, service_name: str):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            message=f"Service '{service_name}' is unavailable",
            code="service_unavailable",
        )
