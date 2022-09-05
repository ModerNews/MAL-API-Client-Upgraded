import re
import secrets
import os
import datetime
import logging

from .request_handler import APICaller
from .anime import Anime
from .my_list import MyList
# from .boards import Boards
from .manga import Manga
from .exceptions import AuthorizationError

__all__ = ['generate_token', 'Client', 'setup_logging']


def generate_token(client_id: str,
                   client_secret: str) -> dict[str, str]:
    """

    Helper function to generate access token **do not use this to refresh token**

    :ivar str client_id: your client id (available on myanimelist developer page)
    :ivar str client_secret: your client secret (available on myanimelist developer page)
    :return: Freshly generated Access Token for your client
    :rtype: dict[str, str]
    """
    token = secrets.token_urlsafe(100)
    code_verifier = code_challenge = token[:128]

    # This is just to keep sure token is long enough, if you didn't change anything round here it should not raise an error
    assert 48 <= len(code_verifier) <= 128

    print("Authorization is not fully automated, you will have to press 'ALLOW' and copy paste url that you will be redirected to")
    input("Press Enter to open authorization page...")

    authorization_url = f"https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={client_id}&state=RequestID42&code_challenge={code_challenge}&code_challenge_method=plain"
    os.system(f"explorer \"{authorization_url}\"")
    print(f"If opening url failed enter it manually into your browser:\n{authorization_url}")
    code_url = input("Paste url you were redirected to\n")
    code = re.search(r"(?<=code=)(\w+)", code_url).group()

    assert code

    base_url = "https://myanimelist.net/v1/"
    uri = "oauth2/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    api_handler = APICaller(base_url=base_url, headers=headers)
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "code_verifier": code_verifier,
        "grant_type": "authorization_code"
    }

    return api_handler.call(uri=uri, method="post", data=data)


def setup_logging(*, format: str = None, filename: str = None, log_level: logging = logging.INFO):
    """
    This is helper function for setting up request logging, all parameters are optional and function may be executed as is
    :param str format: Python Logging library format in which each event will be logged
    :param str filename: filename under which log will be saved, default if malclient_log_{date}.log
    :param log_level: Messages which are less severe than log-level will be ignored, most request have level INFO
    """
    if format is None:
        format = "%(levelname)s | %(asctime)s | %(message)s"
    now = datetime.datetime.now()
    if filename is None:
        filename = f"malclient_log_{now.strftime('%Y-%m-%d_%H-%M')}.log"
    with open(filename, "a+") as file:
        file.write("#Software: Malclient-Upgraded 1.2.5\n")
        file.write(f"#Start-Date: {now.strftime('%Y-%m-%d %H:%M:%S.%f %Z')}\n")
    logging.basicConfig(filename=filename, level=log_level, format=format)


class Client(Anime, Manga, MyList):
    """

    Base class for interacting with MyAnimeList REST API

    :ivar client_id: string containing client_id obtained from [client configuration on MAL](https://myanimelist.net/apiconfig)
    :ivar access_token: string containing access token obtained through OAuth2
    :ivar refresh_token: string containing refresh token obtained through OAuth2
    """
    def __init__(self, *, client_id: str = None, access_token: str = None, refresh_token: str = None, nsfw: bool = False):
        self.nsfw = nsfw
        self._base_url = "https://api.myanimelist.net/"
        self._version = "v2"
        self._base_url = self._base_url + f'{self._version}/'
        self._bearer_token = access_token
        self._client_id = client_id
        self.refresh_token = refresh_token
        self.authorized = False
        self._api_handler = None
        self.headers = {}
        self._connect_to_api()

    def _connect_to_api(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if self._bearer_token is not None:
            self.headers['Authorization'] = f'Bearer {self._bearer_token}'
            self._api_handler = APICaller(base_url=self._base_url,
                                          headers=self.headers)
            self.authorized = True
        elif self._client_id is not None:
            self.headers['X-MAL-CLIENT-ID'] = self._client_id
        else:
            raise AuthorizationError()

        self._api_handler = APICaller(base_url=self._base_url,
                                      headers=self.headers)

    def refresh_bearer_token(self,
                             client_id: str,
                             client_secret: str,
                             refresh_token: str) -> None:
        """

        Function to automatically refresh your clients bearer token (as for now there is no such thing as lifetime token)

        :param str client_id: Your client id number
        :param str client_secret: Your client secret
        :param str refresh_token: Your refresh token
        """
        base_url = "https://myanimelist.net/v1/"
        uri = "oauth2/token"
        headers = {
            'Authorization': f'Bearer {self._bearer_token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'basic {}'
        }
        api_handler = APICaller(base_url=base_url, headers=headers)
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret
        }

        # print response json of authentication, reinstantiate caller method.
        response = api_handler.call(uri=uri, method="post", data=data)
        print("Refreshing token with client id and secret:")
        print(response)
        self._bearer_token = response["access_token"]
        self.refresh_token = response["refresh_token"]
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {response["access_token"]}',
            'X-MAL-Client-ID': '{}'
        }
        self._api_handler = APICaller(base_url=self._base_url,
                                      headers=self.headers)
        return
