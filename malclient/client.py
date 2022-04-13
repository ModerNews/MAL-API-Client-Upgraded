import re

from .request_handler import APICaller
from .anime import Anime
from .my_list import MyList
from .boards import Boards
from .manga import Manga
import requests
import logging
import secrets
import os

__all__ = ['generate_token', 'Client']


def generate_token(client_id: str,
                   client_secret: str) -> dict[str, str]:
    """

    Helper function to generate access token **do not use this to refresh token**

    :ivar str client_id: your client id (available on myanimelist developer _page)
    :ivar str client_secret: your client secret (available on myanimelist developer _page)
    :return: Freshly generated Access Token for your client
    :rtype: dict[str, str]
    """
    token = secrets.token_urlsafe(100)
    code_verifier = code_challenge = token[:128]

    # This is just to keep sure token is long enough, if you didn't change anything round here it should not raise an error
    assert 48 <= len(code_verifier) <= 128

    print("Authorization is not fully userless, you will have to press 'ALLOW' and copy paste url that you will be redirected to")
    input("Press Enter to open authorization _page...")

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


class Client(Anime, Manga, MyList):
    """

    Base class for interacting with MyAnimeList REST API

    :ivar access_token: string containing access token obtained through OAuth2
    :ivar refresh_token: string containing refresh token obtained through OAuth2
    """
    def __init__(self, *, access_token: str, refresh_token: str = None, nsfw: bool = False):
        self.nsfw = nsfw
        self._base_url = "https://api.myanimelist.net/"
        self._version = "v2"
        self._base_url = self._base_url + f'{self._version}/'
        self.bearer_token = access_token
        self.refresh_token = refresh_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.bearer_token}'
        }
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
            'Authorization': f'Bearer {self.bearer_token}',
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
        self.bearer_token = response["access_token"]
        self.refresh_token = response["refresh_token"]
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {response["access_token"]}',
            'X-MAL-Client-ID': '{}'
        }
        self._api_handler = APICaller(base_url=self._base_url,
                                      headers=self.headers)
        return
