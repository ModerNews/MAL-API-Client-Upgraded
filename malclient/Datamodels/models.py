from __future__ import annotations
import datetime
from typing import Union, Optional

from pydantic import BaseModel, HttpUrl

from .enums import *
from .pagination import PagedResult
from ..exceptions import NotFound

__all__ = ['Asset', 'Node', 'AnimeSeason', 'Genre', 'Studio', 'Broadcast', 'Statistics', 'Relation', 'Recommendation',
           'MyMangaListStatus', 'MyAnimeListStatus', 'AnimeObject', 'MangaObject', 'UserAnimeStatistics', "User",
           'ForumTopicDetail', 'ForumTopic', 'ForumCategory', 'ForumAuthor', 'ForumPoll', 'ForumPollOption',
           'ForumPost', 'ForumBoard', 'ForumSubboard']


class MALBaseModel(BaseModel):
    """
    Helper model class used to generate all models used by this API
    """

    class Config:
        arbitrary_types_allowed = True


class Asset(MALBaseModel):
    """

    Asset object, commonly representing an image with two resolutions

    """
    large: Optional[HttpUrl]
    medium: HttpUrl

    def __str__(self):
        return self.medium


class Node(MALBaseModel):
    """

    Object representing simplified anime/manga info

    """
    id: int
    title: str
    main_picture: Optional[Asset]

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return id == other.id


class AnimeSeason(MALBaseModel):
    """

    Representation of anime season (f.e. winter 2022)

    """
    year: int
    season: str

    def __str__(self):
        return f'{self.season} {self.year}'

    def __eq__(self, other):
        return self.year == other.year and self.season == other.season


class Genre(BaseModel):
    """

    Anime or Manga Genre

    """
    id: int
    name: str

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return id == other.id


class Studio(MALBaseModel):
    """

    Representation of anime studio

    """
    id: int
    name: str

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id


class Broadcast(MALBaseModel):
    """

    Object representing date of episode broadcast (in JST)

    """
    day_of_the_week: str
    start_time: Optional[datetime.time]


class Statistics(MALBaseModel):
    """

    Object representing list statistics of anime on MAL
    """
    num_list_users: int
    watching: int
    completed: int
    on_hold: int
    dropped: int
    plan_to_watch: int

    def __init__(self, **data):
        if 'status' in data.keys():
            data = data['status'] | {'num_list_users': data['num_list_users']}
        super().__init__(**data)


class Relation(MALBaseModel):
    """

    Object representing relations between anime and/or manga

    """
    node: Node
    relation_type: str
    relation_type_formatted: str


class Recommendation(MALBaseModel):
    """

    Representation of anime or manga recommendation

    """
    num_recommendations: int
    node: Node


class MyMangaListStatus(MALBaseModel):
    """

    Status from users manga list

    """
    score: Optional[int]
    status: Optional[str]
    is_rereading: Optional[bool]
    updated_at: Union[datetime.datetime, str, None]
    num_chapters_read: Optional[int]
    num_volumes_read: Optional[int]
    start_date: Union[datetime.date, str, None]
    finish_date: Union[datetime.date, str, None]
    priority: Optional[int]
    num_times_reread: Optional[int]
    reread_value: Optional[int]
    tags: Optional[list[str]]
    comments: Optional[str]


class MyAnimeListStatus(MALBaseModel):
    """

    Status from users anime list

    """
    score: int
    status: str
    is_rewatching: bool
    updated_at: Union[datetime.datetime, str]
    num_episodes_watched: int
    start_date: Union[datetime.date, str, None]
    finish_date: Union[datetime.date, str, None]


class AnimeObject(MALBaseModel):
    """

    Model of anime fetched from myanimelist

    """
    id: Optional[int]
    title: Optional[str]
    main_picture: Optional[Asset]
    alternative_titles: Optional[dict]
    start_date: Union[datetime.date, str, None]
    end_date: Union[datetime.date, str, None]
    synopsis: Optional[str]
    mean: Optional[float]
    rank: Optional[int]
    popularity: Optional[int]
    num_list_users: Optional[int]
    num_scoring_users: Optional[int]
    nsfw: Optional[Nsfw]
    genres: Union[list[Genre], None]  # There are series that have no genres on database, like this: 'Katsudou Shashin'
    created_at: Union[datetime.datetime, str, None]
    updated_at: Union[datetime.datetime, str, None]
    media_type: Union[AnimeType, str, None]
    status: Optional[AnimeStatus]
    my_list_status: Optional[MyAnimeListStatus]
    num_episodes: Optional[int]
    start_season: Optional[AnimeSeason]
    broadcast: Optional[Broadcast]
    source: Optional[Union[AnimeSource, str]]
    average_episode_duration: Optional[int]
    rating: Optional[Rating]
    studios: Optional[list[Studio]]
    pictures: Optional[list[Asset]]
    background: Optional[str]
    related_anime: Optional[list[Relation]]
    related_manga: Optional[list[Relation]]
    recommendations: Optional[list[Recommendation]]
    statistics: Optional[Statistics]

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.title


class MangaObject(MALBaseModel):
    """

    Model of manga fetched from myanimelist
    Some fields may not be mentioned in official documentation

    """
    id: Optional[int]
    title: Optional[str]
    main_picture: Optional[Asset]
    alternative_titles: Optional[dict]
    start_date: Union[str, datetime.date, None]  # strptime(d['start_date'], '%Y-%m-%d').date()
    end_date: Union[str, datetime.date, None]  # strptime(d['end_date'], '%Y-%m-%d').date()
    synopsis: Optional[str]
    mean: Optional[float]
    rank: Optional[int]
    popularity: Optional[int]
    num_list_users: Optional[int]
    num_scoring_users: Optional[int]
    nsfw: Optional[Nsfw]
    genres: Optional[list[Genre]]
    created_at: Union[datetime.datetime, str, None]  # strptime(d['created_at'], '%Y-%m-%dT%H:%M:%S%z')
    updated_at: Union[datetime.datetime, str, None]  # strptime(d['updated_at'], '%Y-%m-%dT%H:%M:%S%z')
    media_type: Union[MangaType, str, None]
    status: Union[MangaStatus, str, None]
    my_list_status: Optional[MyMangaListStatus]
    num_volumes: Optional[int]
    num_chapters: Optional[int]
    pictures: Optional[list[Asset]]
    background: Optional[str]
    related_anime: Optional[list[Relation]]
    related_manga: Optional[list[Relation]]
    recommendations: Optional[list[Recommendation]]

    def __eq__(self, other):
        return id == other.id

    def __str__(self):
        return self.title


class UserAnimeStatistics(MALBaseModel):
    num_items_watching: int
    num_items_completed: int
    num_items_on_hold: int
    num_items_dropped: int
    num_items_plan_to_watch: int
    num_items: int
    num_days_watched: float
    num_days_watching: float
    num_days_completed: float
    num_days_on_hold: float
    num_days_dropped: float
    num_days: float
    num_episodes: int
    num_times_rewatched: int
    mean_score: float


class User(MALBaseModel):
    id: int
    name: str
    picture: str
    gender: Optional[str]
    birthday: Union[datetime.date, str, None]
    location: Optional[str]
    joined_at: Union[datetime.datetime, str, None]
    time_zone: Optional[str]
    is_supporter: Optional[bool]
    anime_statistics: Optional[UserAnimeStatistics]


class ForumAuthor(MALBaseModel):
    id: int
    name: str
    forum_avator: Optional[str]  # It is not a typo, goddamn MAL


class ForumTopicDetail(PagedResult):
    """
    Object represents details about forum topic on MAL, has paging support for list of posts

    :ivar str title: Forum topic Title
    :ivar list[ForumPost] posts: List of posts in forum topic, with paging support
    :ivar list[ForumPoll] polls: List of polls available in forum topic
    """
    def __init__(self, title: str = None, posts: list[dict] = None, polls: list[dict] = None, paging_data: dict = {}):
        self.title = title
        self.posts = [ForumPost(**post) for post in posts] if posts else None
        self.polls = [ForumPoll(**poll) for poll in polls] if polls else None
        self._data = {
            'base_class': ForumTopicDetail,
            'next': paging_data.get("next", None),
            'previous': paging_data.get("previous", None)
        }

    def fetch_next_page(self, client):
        """
        Fetches next page of posts, parameters (limit) stay unchanged

        :param Client client: Client with which will be used for fetch
        :returns: New Forum Topic Detail object containing next page of posts
        :rtype: FormTopicDetail
        """
        try:
            assert self._data['next'] is not None
            result = client._api_handler.call(uri=self._data['next'].replace(client._base_url, ''))
        except AssertionError:
            raise NotFound("There is no next page for this query")
        return ForumTopicDetail(paging_data=result['paging'], **result['data'])

    def fetch_previous_page(self, client):
        """
        Fetches previous page of posts, parameters (limit) stay unchanged

        :param Client client: Client with which will be used for fetch
        :returns: New Forum Topic Detail object containing next page of posts
        :rtype: FormTopicDetail
        """
        try:
            assert self._data['previous'] is not None
            result = client._api_handler.call(uri=self._data['previous'].replace(client._base_url, ''))
        except AssertionError:
            raise NotFound("There is no next page for this query")
        return ForumTopicDetail(paging_data=result['paging'], **result['data'])

    def __repr__(self):
        return self.title + ", " + repr(self.posts) + ", " + repr(self.polls)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if type(self) == type(other):
            return self.title == other.title and self.posts == other.posts
        return False


class ForumTopic(MALBaseModel):
    id: int
    title: str
    created_at: Union[datetime.datetime, str]
    created_by: ForumAuthor
    number_of_posts: int
    last_post_created_at: Union[datetime.date, str]
    is_locked: bool


class ForumPollOption(MALBaseModel):
    id: int
    text: str
    votes: int


class ForumPoll(MALBaseModel):
    id: int
    question: str
    close: bool
    options: list[ForumPollOption]


class ForumPost(MALBaseModel):
    id: int
    number: int
    created_at: Union[datetime.datetime, str]
    created_by: ForumAuthor
    body: str
    signature: str


class ForumSubboard(MALBaseModel):
    id: int
    title: str


class ForumBoard(MALBaseModel):
    id: int
    title: str
    description: str
    subboards: list[ForumSubboard]


class ForumCategory(MALBaseModel):
    title: str
    boards: list[ForumBoard]
