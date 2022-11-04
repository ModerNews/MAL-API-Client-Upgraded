import datetime
from typing import Union, Literal, Optional

from .Datamodels import MyAnimeListSorting, MyMangaListSorting, MyAnimeListStatus, MyMangaListStatus, Fields, UserFields, User, MangaObject, AnimeObject, PagedResult, ListStatusFields
from .exceptions import MainAuthRequiredError

__all__ = ["MyList"]


class MyList:

    def __init__(self):
        return

    def update_my_anime_list_status(self, anime_id: int, *,
                                    status: Optional[Literal["watching", "completed", "on_hold", "dropped", "plan_to_watch"]] = None,
                                    start_date: Optional[datetime.date] = None,
                                    finish_date: Optional[datetime.date] = None,
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

        :param int anime_id: id of anime you want to update
        :param Literal["watching", "completed", "on_hold", "dropped", "plan_to_watch"] status: Watching status of series
        :params datetime.date start_date: Start watching date
        :params datetime.date finish_date: Finish watching date
        :param bool is_rewatching: Defines if series is watched multiple times by user
        :param int score: score in 1 to 10 scale
        :param int num_watched_episodes: Number of episodes watched by user
        :param int priority: Priority level to watch this anime
        :param int num_times_rewatched: Number of how many times you've re-watched this series, this should not include first time you completed this series
        :param int rewatch_value: How likely are you to re-watch this series
        :param str tags: Tags you're willing to give to this series
        :param str comments: Additional comments you'd like to leave under this series
        :returns: Updated entry
        :rtype: MyAnimeListStatus
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        if score is not None:
            if 0 > score > 10:
                raise ValueError("Score must be in range 1 - 10")
        data = {
            'status': status,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'finish_date': finish_date.strftime('%Y-%m-%d'),
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
        """
        Deletes entry from list for given anime

        :params int manga_id: ID number for anime you want to delete
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'anime/{anime_id}/my_list_status'
        return self._api_handler.call(method="delete", uri=uri)

    def get_user_anime_list(self, username: str ="@me", *,
                            sort: Union[MyAnimeListSorting, str, None] = None,
                            status: Optional[str] = None,
                            limit: int = 100,
                            offset: int = 0,
                            list_status_fields: ListStatusFields = ListStatusFields.anime_base(),
                            fields: Fields = Fields.from_list(['id', 'title', 'main_picture', 'my_list_status']),
                            nsfw: bool = None):
        """
        Fetches anime list for given user

        :params MyAnimeListSorting sort: Method using which entries will be sorted
        :params str status: Only entries with provided status will be returned
        :params int limit: Number of entries returned
        :params int offset: Position starting from which entries will be fetched
        :params ListStatusFields list_status_fields: Fields returned inside my_list_status field in entry
        :params Fields fields: Fields returned alongside each entry
        :param bool nsfw: If set to True results with nsfw grade 'gray' and 'black' will also be fetched, if omitted it will be inherited from Client class

        :returns: List of objects containing manga information for entries on users' manga list
        :rtype: PagedResult[AnimeObject]
        """
        uri = f'users/{username}/animelist'
        fields.my_list_status = list_status_fields
        if not sort:
            sort = MyAnimeListSorting.LIST_SCORE
        elif isinstance(sort, str):
            sort = MyAnimeListSorting(sort.lower())

        params = {
            "sort": sort.value,
            "limit": limit,
            "fields": fields.to_payload(),
            "status": status,
            "offset": offset,
            "nsfw": nsfw if nsfw is not None else self.nsfw
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult([AnimeObject(**entry) for entry in temp['data']], temp['paging'])

    def get_user_info(self, user_id: Union[str, int] = "@me", fields: UserFields = UserFields.basic()):
        """
        Gets full information about mentioned user, currently you can fetch info only about authenticated user

        :params str user_id: ID of user you want to fetch data for, currently only supports value @me
        :params UserFields fields: Fields to be fetched alongside main data
        :returns: Data for authenticated user
        :rtype: User
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'users/{user_id}'
        params = {"fields": fields.to_payload()}
        return User(**self._api_handler.call(uri, params=params))

    def update_my_manga_list_status(self, manga_id, *,
                                    status: Optional[Literal["reading", "completed", "on_hold", "dropped", "plan_to_read"]] = None,
                                    start_date: Optional[datetime.date] = None,
                                    finish_date: Optional[datetime.date] = None,
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

        :param int manga_id: id of manga you want to update
        :param Literal["watching", "completed", "on_hold", "dropped", "plan_to_watch"] status: Watching status of series
        :params datetime.date start_date: Start reading date
        :params datetime.date finish_date: Finish reading date
        :param bool is_rereading: Defines if series is read multiple times by user
        :param int score: score in 1 to 10 scale
        :param int num_volumes_read: Number of volumes read by user
        :param int num_chapters_read: Number of chapters read by user
        :param int priority: Priority level to watch this anime
        :param int num_times_reread: Number of how many times you've re-read this series, this should not include first time you completed this series
        :param int reread_value: How likely are you to re-read this series
        :param str tags: Tags you're willing to give to this series
        :param str comments: Additional comments you'd like to leave under this series
        :returns: Updated entry
        :rtype: MyMangaListStatus
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'manga/{manga_id}/my_list_status'
        data = {
            'status': status,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'finish_date': finish_date.strftime('%Y-%m-%d'),
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

    def delete_my_manga_list_status(self, manga_id: int):
        """
        Deletes entry from list for given manga

        :params int manga_id: ID number for manga you want to delete
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = f'manga/{manga_id}/my_list_status'
        return self._api_handler.call(method="delete", uri=uri)

    def get_user_manga_list(self, username: str ="@me", *,
                            sort: Union[MyMangaListSorting, str] = MyMangaListSorting.LIST_SCORE,
                            status: Optional[str] = None,
                            limit: int = 100,
                            offset: int = 0,
                            list_status_fields: ListStatusFields = ListStatusFields.manga_base(),
                            fields: Fields = Fields.from_list(['id', 'title', 'main_picture']),
                            nsfw: bool = None):
        """
        Fetches manga list for given user

        :params MyMangaListSorting sort: Method using which entries will be sorted
        :params str status: Only entries with provided status will be returned
        :params int limit: Number of entries returned
        :params int offset: Position starting from which entries will be fetched
        :params ListStatusFields list_status_fields: Fields returned inside my_list_status field in entry
        :params Fields fields: Fields returned alongside each entry
        :param bool nsfw: If set to True results with nsfw grade 'gray' and 'black' will also be fetched, if omitted it will be inherited from Client class

        :returns: List of objects containing manga information for entries on users manga list
        :rtype: PagedResult[MangaObject]
        """
        uri = f'users/{username}/mangalist'
        fields.my_list_status = list_status_fields
        if isinstance(sort, str):
            sort = MyMangaListSorting(sort.lower())
        params = {
            "sort": sort.value,
            "limit": limit,
            "fields": fields.to_payload(),
            "status": status,
            "offset": offset,
            "nfsw": nsfw if nsfw is not None else self.nsfw
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult([MangaObject(**entry) for entry in temp['data']], temp['paging'])