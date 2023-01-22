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

    @staticmethod
    def _parse_response(response, method):
        if method in ["get", "post", "patch", "put"]:
            response_json = response.json()
            if response_json and "data" in response_json:
                list_response = []
                if isinstance(response_json["data"], list):
                    for json_obj in response_json["data"]:
                        new_dict = {}
                        if "node" in json_obj:
                            new_dict = new_dict | json_obj['node']
                            for k, v in new_dict.items():
                                if isinstance(v, dict) and "node" in v and len(v) == 1:
                                    new_dict[k] = new_dict[k]['node']
                        if "list_status" in json_obj:
                            new_dict = new_dict | {'list_status': json_obj['list_status']}
                        if "ranking" in json_obj:
                            new_dict = new_dict | {'ranking': json_obj['ranking']}
                        list_response.append(new_dict if new_dict != {} else json_obj)
                elif isinstance(response_json["data"], dict):
                    list_response = response_json["data"]

                if "paging" in response_json:
                    list_response = {"data": list_response, "paging": response_json["paging"]}
                return list_response
            else:
                return response_json
        elif method == "delete":
            return response.status_code

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



