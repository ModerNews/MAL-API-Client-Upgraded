import datetime
from enum import Enum
from typing import Union, Optional

from pydantic import BaseModel

__all__ = ['Genre', 'Asset', 'Nsfw', 'Broadcast', 'Node', 'Relation', 'RelationType', 'AnimeListStatus', 'Rating',
           'Recommendation', 'Season', 'Studio', 'Author', 'MyAnimeListStatus', 'AnimeType', 'AnimeStatus', 'Source',
           'AnimeObject', 'MyMangaListStatus', 'MangaType', 'MangaStatus', 'MangaObject']


class MALBaseModel(BaseModel):
    """Base model used to generate all models used by this API"""
    class Config:
        arbitrary_types_allowed = True


class Genre(BaseModel):
    """
    Anime or Manga Genre

    :ivar id: id on myanimelist
    :ivar name: name of the genre
    """
    id: int
    name: str

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return id == other.id


class Asset(MALBaseModel):
    """
    Asset object, commonly representing an image with two resolutions

    :ivar large: large resolution of image (can be null)
    :ivar medium: standard image resolution
    """
    large: Optional[str]
    # TODO str with url validator
    medium: str

    def __str__(self):
        return self.medium


class Nsfw(Enum):
    """
    Enumerator representing nsfw stages:
    White
    Gray
    Black
    """
    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Broadcast(MALBaseModel):
    """
    Object representing date of episode broadcast (in JST)

    :ivar day_of_the_week: day of the week on which new episode was broadcast
    :ivar start_time: exact time of episode start
    """
    day_of_the_week: str
    start_time: datetime.time


class Node(MALBaseModel):
    """
    Object representing simplified anime/manga info

    :ivar id: id on myanimelist
    :ivar title: title of anime/manga
    :ivar main_picture: Asset object containing anime/manga cover
    """
    id: int
    title: str
    main_picture: Asset

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return id == other.id


class Relation(MALBaseModel):
    """
    Object representing relations between anime and/or manga

    :ivar node: node of related anime/manga
    :ivar relation_type: representing how those two are related
    :ivar relation_type_formatted: relation_tpye as formatted string
    """
    node: Node
    relation_type: str
    relation_type_formatted: str


class RelationType(Enum):
    """
    Enumerator representing possible relation types between anime and/or manga:
    Sequel
    Prequel
    Alternative Version
    Alternative Setting
    Side Story
    Parent Story
    Summary
    Full Story
    """
    Sequel = "sequel"
    Prequel = "prequel"
    Alt_Setting = "alternative_setting"
    Alt_Version = "alternative_version"
    Side_Story = "side_story"
    Parent_Story = "parent_story"
    Summary = "summary"
    Full_Story = "full_story"


# Not used anywhere yet
class AnimeListStatus(MALBaseModel):
    """
    Status from users anime list

    :ivar node: node of anime this entry represents
    :ivar score: score given by user
    :ivar status: status set by user (watching, finished, plan to watch)
    :ivar is_rewatching: if user is rewatching series
    :ivar num_episodes_watched: number of episodes watched by user
    :ivar updated_at: date and time of last update
    """
    Node: Node
    score: int
    status: str
    is_rewatching: bool
    updated_at: Union[datetime.datetime, str]
    num_episodes_watched: int


class Rating(Enum):
    """
    Rating of shows provided by myanimelist:
    G - All Ages
    PG - Children
    PG_13 - Teens 13 and Older
    R - 17+ (violence & profanity)
    RR - Profanity & Mild Nudity
    Rx - Hentai
    """
    G = 'g'
    PG = 'pg'
    PG_13 = 'pg_13'
    R = 'r'
    RR = 'r+'
    Rx = 'rx'


class Recommendation(MALBaseModel):
    """
    Representation of anime recommendation

    :ivar node: node of the recommended anime/manga
    :ivar num_recommendations: number of users recommending this manga/anime
    """
    num_recommendations: int
    node: Node


class Season(MALBaseModel):
    """
    Representation of anime season (f.e. winter 2022)

    :ivar year: Year of the season
    :ivar season: one of seasons (winter, spring, summer, fall)
    """
    year: int
    season: str

    def __str__(self):
        return f'{self.season} {self.year}'

    def __eq__(self, other):
        return self.year == other.year and self.season == other.season


class Studio(MALBaseModel):
    """
    Representation of anime studio

    :ivar id: Id available on myanimelist
    :ivar name: Name of studio
    """
    id: int
    name: str

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id


# Unused, unsure what this exactly is
class Author(MALBaseModel):
    """
    Representation of
    """
    id: int
    first_name: str
    last_name: str
    role: str

    def __eq__(self, other):
        return self.role == other.role and id == other.id


class MyAnimeListStatus(MALBaseModel):
    """
        Status from users anime list

        :ivar score: score given by user
        :ivar status: status set by user (watching, finished, plan to watch)
        :ivar is_rewatching: if user is rewatching series
        :ivar num_episodes_watched: number of episodes watched by user
        :ivar updated_at: date and time of last update
    """
    status: str
    score: int
    num_episodes_watched: int
    is_rewatching: bool
    updated_at: Union[datetime.datetime, str] #  Union[datetime.datetime, str].strptime(updated_at, '%Y-%m-%dT%H:%M:%S%z')


class AnimeType(Enum):
    """
    Enumerator representing anime type:
    Unknown
    TV - streamed in Japanese TV
    OVA - Original Video Animation
    Movie - animated movie
    Special - special for anime
    ONA - Original Net Anime
    Music - music anime
    """
    Unknown = "unknown"
    TV = "tv"
    OVA = 'ova'
    Movie = 'movie'
    Special = 'special'
    ONA = 'ona'
    Music = 'Music'


class AnimeStatus(Enum):
    """
    Enumerating representing current anime status
    Finished Airing
    Currently Airing
    Not Yet Aired
    """
    Finished = 'finished_airing'
    Airing = 'currently_airing'
    Not_Yet_Aired = 'not_yet_aired'


class Source(Enum):
    """
    Enumerator representing source of anime:
    Other
    Original
    Manga
    Manga 4 Koma
    Web Manga
    Novel
    Light Novel
    Cisual Novel
    Game
    Card Game
    Book
    Picture Book
    Radio
    Music
    """
    Other = "other"
    Original = "original"
    Manga = "manga"
    Manga_4_koma = "4_koma_manga"
    Web_Manga = "web_manga"
    Digital_Manga = "digital_manga"
    Novel = "novel"
    Light_Novel = "light_novel"
    Visual_Novel = "visual_novel"
    Game = "game"
    Card_Game = "card_game"
    Book = "book"
    Picture_Book = "picture_book"
    Radio = "radio"
    Music = "music"


class AnimeObject(MALBaseModel):
    """
    Model of anime fetched from myanimelist

    :ivar id: id on myanimelist
    :ivar title: title of anime
    :ivar main_picture: asset containing anime cover
    :ivar alternative_titles: dictionary of possible alternative titles
    :ivar start_date: date of first airing
    :ivar end_date: date of airing of last episode
    :ivar synopsis: short anime synopsis
    :ivar mean: mean score given by users
    :ivar rank: score rank of series
    :ivar popularity: popularity rank of series
    :ivar num_list_users: number of users having this series on their list
    :ivar num_scoring_users: number of users scoring this series
    :ivar nsfw: nsfw rating
    :ivar genres: list of genres of this series
    :ivar created_at: date and time of creation on myanimelist
    :ivar updated_at: date and time of last update on myanimelist
    :ivar media_type: type of anime
    :ivar status: status of this anime
    :ivar my_list_status: entry from your anime list for this anime
    :ivar num_episodes: number of episodes
    :ivar start_season: season in which series was aired
    :ivar rating: age rating
    :ivar studios: studios taking part in production
    :ivar pictures: all images for this series
    :ivar background: short background description
    :ivar related_anime: other anime series related to this
    :ivar related_manga: manga serializations related to this series
    :ivar recommendations: other anime series recommended by users
    """
    id: int
    title: str
    main_picture: Optional[Asset]
    alternative_titles: Optional[dict]
    start_date: Union[str, datetime.date] #  strptime(d['start_date'], '%Y-%m-%d').date()
    end_date: Union[str, datetime.date] #  strptime(d['end_date'], '%Y-%m-%d').date()
    synopsis: Optional[str]
    mean: Optional[float]
    rank: Optional[int]
    popularity: Optional[int]
    num_list_users: int
    num_scoring_users: int
    nsfw: Optional[Nsfw]
    genres: list[Genre]
    created_at: Union[datetime.datetime, str] #  strptime(d['created_at'], '%Y-%m-%dT%H:%M:%S%z')
    updated_at: Union[datetime.datetime, str] #  strptime(d['updated_at'], '%Y-%m-%dT%H:%M:%S%z')
    media_type: AnimeType
    status: AnimeStatus
    my_list_status: Optional[MyAnimeListStatus]
    num_episodes: int
    start_season: Optional[Season]
    broadcast: Optional[Broadcast]
    source: Optional[Source]
    average_episode_duration: Optional[int]
    rating: Optional[Rating]
    studios: list[Studio]
    pictures: list[Asset]
    background: Optional[str]
    related_anime: list[Relation]
    related_manga: list[Relation]
    recommendations: list[Recommendation]

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.title


class MangaType(Enum):
    """
    Enumerator representing type of manga
    Unknown
    Manga
    Novel
    One Shot
    Doujinshi - self-published manga
    Manhwa - Korean comic
    Manhua - Chinese comic
    OEL - Original English-Language Manga
    """
    Unknown = "unknown"
    Manga = "manga"
    Novel = "novel"
    One_Shot = "one_shot"
    Doujinshi = "doujinshi"
    Manhwa = "manhwa"
    Manhua = "manhua"
    OEL = "oel"


class MyMangaListStatus(MALBaseModel):
    """
        Status from users manga list
        Documentation says about loads more parameters but apparently only those are present:

        :ivar score: score given by user
        :ivar status: status set by user (reading, finished, plan to read)
        :ivar is_rereading: if user is rereading series
        :ivar num_chapters_read: number of chapters read by user
        :ivar num_volumes_read: number of volumes read by user
        :ivar updated_at: date and time of last update
    """
    score: int
    status: str
    is_rereading: bool
    updated_at: Union[datetime.datetime, str] #  Union[datetime.datetime, str].strptime(updated_at, '%Y-%m-%dT%H:%M:%S%z')
    num_chapters_read: int
    num_volumes_read: int
    # Those are fields mentioned by documentation, but not present in response JSON
    # start_date: Union[datetime.date, str, None]
    # finish_date: Union[datetime.date, str, None]
    # priority: int
    # num_times_reread: int
    # reread_value: int
    # tags: list[str]
    # comments: str


class MangaStatus(Enum):
    """
        Enumerating representing current manga status
        Finished
        Currently Publishing
        Not Yet Published
        """
    Finished = 'finished'
    Publishing = 'currently_publishing'
    Not_Yet_Published = 'not_yet_published'


class MangaObject(MALBaseModel):
    """
        Model of manga fetched from myanimelist

        :ivar id: id on myanimelist
        :ivar title: title of manga
        :ivar main_picture: asset containing manga cover
        :ivar alternative_titles: dictionary of possible alternative titles
        :ivar start_date: date of first chapter serialization
        :ivar end_date: date of last chapter serialization
        :ivar synopsis: short manga synopsis
        :ivar mean: mean score given by users
        :ivar rank: score rank of series
        :ivar popularity: popularity rank of series
        :ivar num_list_users: number of users having this series on their list
        :ivar num_scoring_users: number of users scoring this series
        :ivar nsfw: nsfw rating
        :ivar genres: list of genres for this series
        :ivar created_at: date and time of creation on myanimelist
        :ivar updated_at: date and time of last update on myanimelist
        :ivar media_type: type of manga
        :ivar status: status of this manga
        :ivar my_list_status: entry from your manga list for this series
        :ivar num_chapters: number of chapters
        :ivar num_volumes: number of volumes
        :ivar pictures: all images for this series
        :ivar background: short background description
        :ivar related_anime: anime series related to this manga
        :ivar related_manga: other manga serializations related to this series
        :ivar recommendations: other manga recommended by users
    """
    id: int
    title: str
    main_picture: Optional[Asset]
    alternative_titles: Optional[dict]
    start_date: Union[str, datetime.date, None]  # strptime(d['start_date'], '%Y-%m-%d').date()
    end_date: Union[str, datetime.date, None]  # strptime(d['end_date'], '%Y-%m-%d').date()
    synopsis: Optional[str]
    mean: Optional[float]
    rank: Optional[int]
    popularity: Optional[int]
    num_list_users: int
    num_scoring_users: int
    nsfw: Optional[Nsfw]
    genres: list[Genre]
    created_at: Union[datetime.datetime, str]  # strptime(d['created_at'], '%Y-%m-%dT%H:%M:%S%z')
    updated_at: Union[datetime.datetime, str]  # strptime(d['updated_at'], '%Y-%m-%dT%H:%M:%S%z')
    media_type: MangaType
    status: MangaStatus
    my_list_status: Optional[MyMangaListStatus]
    num_volumes: int
    num_chapters: int
    pictures: list[Asset]
    background: Optional[str]
    related_anime: list[Relation]
    related_manga: list[Relation]
    recommendations: list[Recommendation]

    def __eq__(self, other):
        return id == other.id

    def __str__(self):
        return self.title
