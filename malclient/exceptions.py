import json

class APIException(Exception):
    """Base exception for API"""
    def __init__(self, status_code, message, response):
        self.status_code = status_code
        self.message = message
        self.response = response

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.status_code} - {self.message}"


# Those are helper classes to simplify catching exceptions
class BadRequest(APIException):
    """HTTP 400 Bad Request exception"""
    def __init__(self, response):
        super().__init__("400 Bad Request", json.loads(response.text)['message'], response)


class Unauthorized(APIException):
    """HTTP 401 Unauthorized exception"""
    def __init__(self, response):
        super().__init__("401 Unauthorized", json.loads(response.text)['message'], response)


class Forbidden(APIException):
    """HTTP 403 Forbidden exception"""
    def __init__(self, response):
        super().__init__("403 Forbidden", json.loads(response.text)['message'], response)


class NotFound(APIException):
    """HTTP 404 Not Found exception"""
    def __init__(self, response):
        super().__init__("404 Not Found", json.loads(response.text)['message'], response)