from models import *
from typing import Union

class MyList():

    def __init__(self):
        return

    def update_my_anime_list_status(self, anime_id, data):
        """

        Updates myanimelist status for a given anime, takes payload as dictionary as argument.
        Emit fields to not update. Returns response object.
        example input for data:
        ```json
        data = {
        'status': 'watching',
        'is_rewatching': False,
        'score': 0,
        'watched_episodes': 0,
        'priority': 0,
        'num_times_rewatch': 0,
        'rewatch_value': 0,
        'tags': '',
        'comments': ''
        }
        ```

        """
        statuses = ["watching, completed, on_hold, dropped, plan_to_watch"]
        uri = f'anime/{anime_id}/my_list_status'
        return self._api_handler.call(method="patch", uri=uri, data=data)

    # need another function for adding manga to list
    def delete_my_anime_list_status(self, anime_id):
        uri = f'anime/{anime_id}/my_list_status'
        return (self._api_handler.call("delete"))

    def get_user_anime_list(self, username="@me", *, sort: Union[MyListSorting, str] = None, status: str=None, limit: int = 100):
        uri = f'users/{username}/animelist'
        if not sort:
            sort = MyListSorting.ListScore
        elif isinstance(sort, str):
            sort = MyListSorting(sort.lower())
        params = {"sort": sort.value, "limit": limit, "fields": "list_status"}
        if status is not None:
            params['status'] = status
        return self._api_handler.call(uri=uri, params=params)

    def get_user_info(self, user_id="@me"):
        uri = f'users/{user_id}'
        params = {"fields": "anime_statistics"}
        return self._api_handler.call(uri)

    def update_my_manga_list_status(self, manga_id, data):
        """

        Updates myanimelist status for a given manga, takes payload as dictionary as argument.
        Emit fields to not update. Returns response object.
        example input for data:
        ```json
        data = {
        'status': 'watching',
        'is_rereading': False,
        'score': 0,
        'num_volumes_read': 0,
        'num_chapters_read': 0,
        'priority': 0,
        'comments': ''
        }
        ```
        """
        uri = f'manga/{manga_id}/my_list_status'
        statuses = [
            "reading", "completed", "on_hold", "dropped", "plan_to_read"
        ]
        return self._api_handler.call(method="patch", uri=uri, data=data)

    def delete_my_manga_list_status(self, manga_id):
        uri = f'manga/{manga_id}/my_list_status'
        return (self._api_handler.call("delete"))

    def get_user_manga_list(self, username="@me", sort=None, status=None, limit=100):
        uri = f'users/{username}/mangalist'
        sort_options = [
            "list_score", "list_updated_at", "manga_title", "manga_start_date",
            "manga_id"
        ]
        if sort not in sort_options:
            sort = "list_score"
        params = {"sort": sort, "limit": limit, "fields": "list_status"}
        if status is not None:
            params['status'] = status
        return self._api_handler.call(uri=uri, params=params)
