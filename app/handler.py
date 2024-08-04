
""" App handler """
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from core.contracts.handler import Handler as HandlerContract


class Handler(HandlerContract):
    """Exception class for the application."""

    def handle_exception(self, exception: Exception) -> None:
        """
        Handler function to handle exceptions
        """
        file = exception.__traceback__.tb_frame.f_globals.get('__file__')
        line = exception.__traceback__.tb_lineno
        message = f"File: {file}, Line: {line}, Exception: {exception}"

        print(message)

    def handle_api_exception(self, request: Request, exc: Exception) -> JSONResponse:
        """
        Handler function to handle exceptions
        """
        error_message = str(exc)

        # Return a JSON response with error details
        return JSONResponse(
            status_code=500,
            content={"error": error_message},
        )

    def handle_api_validation_exception(self, request: Request, exc: RequestValidationError) -> JSONResponse:
        """
        Handler function to handle API exceptions
        """
        errors = exc.errors()
        formatted_errors = []

        for error in errors:
            formatted_error = {
                "type": error["type"],
                "message": error["msg"],
                "input": error["input"],
            }
            formatted_errors.append(formatted_error)

        return JSONResponse(
            status_code=422,
            content={"errors": formatted_errors},
        )
