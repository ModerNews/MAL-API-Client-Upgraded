from typing import Union, Literal, Optional

from .Datamodels import MyAnimeListSorting, MyMangaListSorting, MyAnimeListStatus, MyMangaListStatus
from .exceptions import MainAuthRequiredError

__all__ = ["MyList"]


class MyList:

    def __init__(self):
        return

    def update_my_anime_list_status(self, anime_id, *,
                                    status: Optional[Literal["watching", "completed", "on_hold", "dropped", "plan_to_watch"]] = None,
                                    is_rewatching: Optional[bool] = None,
                                    score: Optional[int] = None,
                                    num_watched_episodes: Optional[int] = None,
                                    priority: Optional[int] = None,
                                    num_times_rewatched: Optional[int] = None,
                                    rewatch_value: Optional[int] = None,
                                    tags: Optional[str] = None,
                                    comments: Optional[str] = None, **kwargs):
        """

        Updates myanimelist status for a given anime, takes payload as dictionary as argument.
        Emit fields to not update. Returns updated entry from list.

        """
        if not self.authorized:
            raise MainAuthRequiredError()
        data = {
            'status': status,
            'is_rewatching': is_rewatching,
            'score': score,
            'num_watched_episodes': num_watched_episodes,
            'priority': priority,
            'num_times_rewatch': num_times_rewatched,
            'rewatch_value': rewatch_value,
            'tags': tags,
            'comments': comments
        }
        uri = f'anime/{anime_id}/my_list_status'
        return MyAnimeListStatus(**self._api_handler.call(method="patch", uri=uri, data=data | kwargs))

    # need another function for adding manga to list
    def delete_my_anime_list_status(self, anime_id):
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'anime/{anime_id}/my_list_status'
        return self._api_handler.call("delete")

    def get_user_anime_list(self, username="@me", *, sort: Union[MyAnimeListSorting, str] = None, status: str = None, limit=100, additional_fields=None):
        if additional_fields is None:
            additional_fields = []
        uri = f'users/{username}/animelist'
        if not sort:
            sort = MyAnimeListSorting.ListScore
        elif isinstance(sort, str):
            sort = MyAnimeListSorting(sort.lower())
        params = {"sort": sort.value, "limit": limit, "fields": ",".join(["list_status"] + additional_fields)}
        if status is not None:
            params['status'] = status
        return self._api_handler.call(uri=uri, params=params)

    def get_user_info(self, user_id="@me"):
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'users/{user_id}'
        params = {"fields": "anime_statistics"}
        return self._api_handler.call(uri)

    def update_my_manga_list_status(self, manga_id, *,
                                    status: Optional[Literal["reading", "completed", "on_hold", "dropped", "plan_to_read"]] = None,
                                    is_rereading: Optional[bool] = None,
                                    score: Optional[int] = None,
                                    num_volumes_read: Optional[int] = None,
                                    num_chapters_read: Optional[int] = None,
                                    priority: Optional[int] = None,
                                    num_times_reread: Optional[int] = None,
                                    reread_value: Optional[int] = None,
                                    tags: Optional[str] = None,
                                    comments: Optional[str] = None, **kwargs):
        """

        Updates myanimelist status for a given manga, takes payload as dictionary as argument.
        Emit fields to not update. Returns updated entry from list.
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'manga/{manga_id}/my_list_status'
        data = {
            'status': status,
            'is_rereading': is_rereading,
            'score': score,
            'num_volumes_read': num_volumes_read,
            'num_chapters_read': num_chapters_read,
            'priority': priority,
            'num_times_reread': num_times_reread,
            'reread_value': reread_value,
            'tags': tags,
            'comments': comments
        }
        return MyMangaListStatus(**self._api_handler.call(method="patch", uri=uri, data=data | kwargs))

    def delete_my_manga_list_status(self, manga_id):
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'manga/{manga_id}/my_list_status'
        return self._api_handler.call("delete")

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
