import json
from typing import Optional


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


class AuthorizationError(Exception):
    """
    Base for all exceptions raised because of auth problems
    More info: https://myanimelist.net/apiconfig/references/api/v2#section/Authentication
    """
    def __init__(self, message: Optional[str] = None):
        super().__init__("No valid authorization method, use OAuth2 or Client ID" if message is None else message)


class MainAuthRequiredError(AuthorizationError):
    """
    Exception indicates that for action you were trying to perform you need main_auth
    More info: https://myanimelist.net/apiconfig/references/api/v2#section/Authentication
    """
    def __init__(self):
        super().__init__("This endpoint is available only using OAuth2")


# Those are helper classes to simplify catching exceptions
class BadRequest(APIException):
    """HTTP 400 Bad Request exception"""
    def __init__(self, response):
        super().__init__("400 Bad Request", json.loads(response.text).get('message', None), response)


class Unauthorized(APIException):
    """HTTP 401 Unauthorized exception"""
    def __init__(self, response):
        super().__init__("401 Unauthorized", json.loads(response.text).get('message', None), response)


class Forbidden(APIException):
    """HTTP 403 Forbidden exception"""
    def __init__(self, response):
        super().__init__("403 Forbidden", json.loads(response.text).get('message', None), response)


class NotFound(APIException):
    """HTTP 404 Not Found exception"""
    def __init__(self, response):
        super().__init__("404 Not Found", json.loads(response.text).get('message', None), response)
