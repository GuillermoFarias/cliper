""" This module contains the Response class that is used to return responses. """
from fastapi.responses import JSONResponse


class Response:
    """ Response class to handle responses """

    def __init__(self):
        self.default_status = 200
        self.default_message = "Success"

    def success(self, data=None, status_code=None, message=None):
        """Return a success response."""
        status_code = status_code or self.default_status
        message = message or self.default_message
        content = {"data": data}
        return JSONResponse(content=content, status_code=status_code)

    def error(self, message=None, status_code=400):
        """Return an error response."""
        message = message or "An error occurred"
        content = {"status": "error", "message": message}
        return JSONResponse(content=content, status_code=status_code)
