import requests
from .exceptions import *

__all__ = ['APICaller']


class APICaller(object):
    def __init__(self, base_url, headers):
        self._base_url = base_url
        self._headers = headers

    def call(self, uri, method="get", params=None, *args, **kwargs):
        requester = getattr(requests, method.lower())
        url = self._base_url + uri
        response = requester(url=url,
                             headers=self._headers,
                             params=params,
                             *args,
                             **kwargs)
        if response.status_code < 400:
            if method in ["get", "post", "patch", "put"]:
                response_json = response.json()
                if response_json and "data" in response_json:
                    list_response = []
                    for json_obj in response_json["data"]:
                        new_dict = {}
                        if "node" in json_obj:
                            for i in json_obj["node"]:
                                new_dict[i] = json_obj["node"][i]
                        if "list_status" in json_obj:
                            for i in json_obj["list_status"]:
                                new_dict[i] = json_obj["list_status"][i]
                        if "ranking" in json_obj:
                            for i in json_obj["ranking"]:
                                new_dict[i] = json_obj["ranking"][i]
                        list_response.append(new_dict)
                    if "paging" in response_json:
                        list_response = {"data": list_response, "paging": response_json["paging"]}
                    return list_response
                else:
                    return response_json
            elif method == "delete":
                return response.status_code
        else:
            if str(response.status_code) == "400" or str(response.status_code).lower() == "400 bad request":
                raise BadRequest(response)
            elif str(response.status_code) == "401" or str(response.status_code).lower() == "401 unauthorized":
                raise Unauthorized(response)
            elif str(response.status_code) == "403" or str(response.status_code).lower() == "403 forbidden":
                raise Forbidden(response)
            elif str(response.dict(response.text)['message']) == "404" or str(response.status_code).lower() == "404 not found":
                raise NotFound(response)
            else:
                raise APIException(response.status_code, json.loads(response.text)['message'], response)



