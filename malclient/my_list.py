from typing import Union, Literal, Optional

from .Datamodels import MyAnimeListSorting, MyMangaListSorting, MyAnimeListStatus, MyMangaListStatus, Fields, UserFields, User, MangaObject, AnimeObject, PagedResult, ListStatusFields
from .exceptions import MainAuthRequiredError

__all__ = ["MyList"]


class MyList:

    def __init__(self):
        return

    def update_my_anime_list_status(self, anime_id: int, *,
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
        if score is not None:
            if 0 > score > 10:
                raise ValueError("Score must be in range 1 - 10")
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
    def delete_my_anime_list_status(self, anime_id: int):
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'anime/{anime_id}/my_list_status'
        return self._api_handler.call(method="delete", uri=uri)

    def get_user_anime_list(self, username: str ="@me", *,
                            sort: Union[MyAnimeListSorting, str, None] = None,
                            status: Optional[str] = None,
                            limit: int = 100,
                            offset: int = 0,
                            list_status_fields: ListStatusFields = ListStatusFields.all(),
                            anime_fields: Fields = Fields.node()):
        uri = f'users/{username}/animelist'
        if not sort:
            sort = MyAnimeListSorting.LIST_SCORE
        elif isinstance(sort, str):
            sort = MyAnimeListSorting(sort.lower())

        params = {
            "sort": sort.value,
            "limit": limit,
            "fields": list_status_fields.to_payload() + anime_fields.to_payload(),
            "status": status,
            "offset": offset
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult([AnimeObject(**entry) for entry in temp['data']], temp['paging'])

    def get_user_info(self, user_id: str = "@me", fields: UserFields = UserFields.basic()):
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'users/{user_id}'
        params = {"fields": fields.to_payload()}
        return User(**self._api_handler.call(uri, params=params))

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
        return self._api_handler.call(method="delete", uri=uri)

    def get_user_manga_list(self, username: str ="@me", *,
                            sort: Union[MyMangaListSorting, str] = MyMangaListSorting.LIST_SCORE,
                            status: Optional[str] = None,
                            limit: int = 100,
                            offset: int = 0,
                            list_status_fields: ListStatusFields = ListStatusFields.all(),
                            manga_fields: Fields = Fields.node()):
        uri = f'users/{username}/mangalist'
        if isinstance(sort, str):
            sort = MyMangaListSorting(sort.lower())
        params = {
            "sort": sort.value,
            "limit": limit,
            "fields": list_status_fields.to_payload() + manga_fields.to_payload(),
            "status": status,
            "offset": offset,
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult([MangaObject(**entry) for entry in temp['data']], temp['paging'])