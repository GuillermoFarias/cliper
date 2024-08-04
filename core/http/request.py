""" Request class to handle request data """
from fastapi import Request as FastAPIRequest


class Request:
    """ Request class to handle request data """
    method: str
    ip: str
    url: str
    headers: dict
    query_params: dict
    path_params: dict
    body: dict

    def __init__(self, request: FastAPIRequest):
        self.request = request
        self.method = request.method
        self.ip = request.client.host
        self.url = request.url.path
        self.headers = dict(request.headers)
        self.query_params = dict(request.query_params)
        self.path_params = dict(request.path_params)

    async def body(self):
        """Get Dic of the request body."""
        return await self.request.body()

    def header(self, key: str):
        """Get a header value from the request."""
        return self.headers.get(key)

    def query_param(self, key: str):
        """Get a query parameter value from the request."""
        return self.query_params.get(key)

    def path_param(self, key: str):
        """Get a path parameter value from the request."""
        return self.path_params.get(key)

    async def get(self, key: str):
        """Get a value from the request body."""
        # body_value = await self.body().
        # if body_value:
        #     return body_value

        param_value = self.query_params.get(key)
        if param_value:
            return param_value

        query_value = self.query_params.get(key)
        if query_value:
            return query_value

        return None
