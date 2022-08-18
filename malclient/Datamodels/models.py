from __future__ import annotations
import datetime
from typing import Union, Optional

from pydantic import BaseModel, HttpUrl

from .enums import *


__all__ = ['Asset', 'Node', 'AnimeSeason', 'Genre', 'Studio', 'Broadcast', 'Statistics', 'Relation', 'Recommendation',
           'MyMangaListStatus', 'MyAnimeListStatus', 'AnimeObject', 'MangaObject']


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
    score: int
    status: str
    is_rereading: bool
    updated_at: Union[datetime.datetime, str]
    num_chapters_read: int
    num_volumes_read: int
    start_date: Union[datetime.date, str, None]
    finish_date: Union[datetime.date, str, None]
    priority: int
    num_times_reread: int
    reread_value: int
    tags: list[str]
    comments: str


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
