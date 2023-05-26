import datetime

import requests
from .exceptions import *
import logging

__all__ = ['APICaller']


class APICaller(object):
    def __init__(self, base_url, headers):
        self._base_url = base_url
        self._headers = headers

    def call(self, uri, method="get", params=None, *args, **kwargs):
        requester = getattr(requests, method.lower())
        url = self._base_url + uri
        logging.info(f"{method.upper()} {url} Query Parameters: {params}")
        response = requester(url=url,
                             headers=self._headers,
                             params=params,
                             *args,
                             **kwargs)
        now = datetime.datetime.now()
        if response.status_code < 400:
            response = self._parse_response(response, method)
        elif 400 <= response.status_code:
            self._parse_error(response, method, url)
        end = datetime.datetime.now()
        return response

    def _parse_response(self, response, method):
        if method in ["get", "post", "patch", "put"]:
            response_json = response.json()
            response_json = self._parse_json(response_json)
            return response_json

        elif method == "delete":
            return response.status_code

    def _parse_json(self, json_obj):
        """
        This is main function that handles whole logic of parsing json response from MAL API.
        It is a little bit messy, so it is heavily commented for better understanding.

        :param json_obj: json object to parse
        """
        # If json_obj is list, then we need to recursively parse every element of it
        if isinstance(json_obj, list):
            list_response = []
            for json_obj in json_obj:
                new_dict = self._parse_json(json_obj)
                list_response.append(new_dict if new_dict != {} else json_obj)
            return list_response

        # Logic for parsing dictionary response
        elif isinstance(json_obj, dict):
            new_dict = json_obj.copy()  # Create copy of json_obj to avoid messing original object

            # Case #1: nodes are representants of anime/manga/character/staff/etc. in nested objects,
            # in fields like: animeography, anime search, anime ranking, etc.
            # Example: https://api.myanimelist.net/v2/characters/161357?fields=animeography
            # Solution: recursively parse node as top level object and merge it with parent
            if "node" in json_obj:
                new_dict = new_dict | json_obj['node']
                for k, v in new_dict.items():
                    if isinstance(v, dict) and "node" in v and len(v) == 1:
                        new_dict[k] = new_dict[k]['node']

            # Case #2: list_status is additional field present in anime/manga lists besides node
            # Example: https://api.myanimelist.net/v2/users/ModerNews/animelist?fields=list_status&limit=5
            # Solution: merge list_status with node and make it a part of AnimeObject object
            if "list_status" in json_obj:
                new_dict = new_dict | {'list_status': json_obj['list_status']}

            # Case #3: ranking is additional field present in anime/manga rankings besides node
            # Example: https://api.myanimelist.net/v2/anime/ranking?ranking_type=bypopularity&limit=5
            # Solution: merge ranking with node and make it a part of AnimeObject object
            if "ranking" in json_obj:
                new_dict = new_dict | {'ranking': json_obj['ranking']}

            # Case #4: role is additional field present in anime/manga characters/staff besides node
            # Example: https://api.myanimelist.net/v2/characters/161357?fields=animeography
            # Solution: merge role with node and make it a part of AnimeObject object
            if "role" in json_obj:
                new_dict = new_dict | {'role': json_obj['role']}

            # Case #5 (pagination): response is paginated and object and is split into data and paging objects
            # Example: https://api.myanimelist.net/v2/anime/ranking?ranking_type=bypopularity&limit=5
            # Solution: parse data object individually (to cover cases such as data being list of elements)
            # and return data and paging objects as one dictionary to be converted into PagedResult object
            if json_obj and "data" in json_obj:
                list_response = self._parse_json(json_obj["data"])
                if "paging" in json_obj:  # Make sure that paging object is present in response
                    json_obj = {"data": list_response, "paging": json_obj["paging"]}
                return json_obj

            # Case #6: animeography is additional field representing anime objects present in character/staff endpoints
            # with node field and additional role field at the top level.
            # Example: https://api.myanimelist.net/v2/characters/161357?fields=first_name,last_name,alternative_name,main_picture,biography,pictures,animeography,num_favorites
            # Solution: recursively parse each entry of animeography list to cover both node and role fields
            if "animeography" in json_obj:
                response_json = json_obj | {'animeography': self._parse_json(json_obj['animeography'])}
                return response_json
            return new_dict

    @staticmethod
    def _parse_error(response, method, url):
        logging.error(f"{method.upper()} {url} {response.status_code} {json.loads(response.text)['error']}: {json.loads(response.text)['message'] if 'message' in json.loads(response.text) or len(json.loads(response.text)) != 0 else ''}")
        if str(response.status_code) == "400" or str(response.status_code).lower() == "400 bad request":
            raise BadRequest(response)
        elif str(response.status_code) == "401" or str(response.status_code).lower() == "401 unauthorized":
            raise Unauthorized(response)
        elif str(response.status_code) == "403" or str(response.status_code).lower() == "403 forbidden":
            raise Forbidden(response)
        elif str(response.status_code) == "404" or str(response.status_code).lower() == "404 not found":
            raise NotFound(response)
        else:
            raise APIException(response.status_code, json.loads(response.text)['message'], response)



