import datetime
from enum import Enum
from typing import Union, Optional
from __future__ import annotations

from pydantic import BaseModel

__all__ = ['Genre', 'Asset', 'Nsfw', 'Broadcast', 'Node', 'Relation', 'RelationType', 'AnimeListStatus', 'Rating',
           'Recommendation', 'Season', 'AnimeSeason', 'Studio', 'MyAnimeListStatus', 'AnimeType', 'AnimeStatus', 'Source',
           'AnimeObject', 'MyMangaListStatus', 'MangaType', 'MangaStatus', 'MangaObject', 'PagedResult', 'RankingType',
           'Sorting', "MyListSorting"]

from malclient import exceptions


class MALBaseModel(BaseModel):
    """
    Base model used to generate all models used by this API
    """
    class Config:
        arbitrary_types_allowed = True


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


class Asset(MALBaseModel):
    """

    Asset object, commonly representing an image with two resolutions

    """
    large: Optional[str]
    # TODO str with url validator
    medium: str

    def __str__(self):
        return self.medium


class Nsfw(Enum):
    """

    Enumerator representing nsfw stages:

    """
    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


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


class Relation(MALBaseModel):
    """

    Object representing relations between anime and/or manga

    """
    node: Node
    relation_type: str
    relation_type_formatted: str


class RelationType(Enum):
    """

    Enumerator representing possible relation types between anime and/or manga:

    """
    Sequel = "sequel"
    Prequel = "prequel"
    Alt_Setting = "alternative_setting"
    Alt_Version = "alternative_version"
    Side_Story = "side_story"
    Parent_Story = "parent_story"
    Summary = "summary"
    Full_Story = "full_story"


class Recommendation(MALBaseModel):
    """

    Representation of anime or manga recommendation

    """
    num_recommendations: int
    node: Node


class PagedResult(list):
    """

    List of objects with paging support

    """
    def __init__(self, seq, page_link: dict):
        self._page = page_link
        super().__init__(seq)

    def fetch_next_page(self, client):
        try:
            result = client._api_handler.call(uri=self._page["next"].replace(client._base_url, ''))
        except KeyError:
            raise exceptions.NotFound("There is no next _page for this query")
        return PagedResult([Node(**temp_object) for temp_object in result["data"]], result["paging"])

    def fetch_previous_page(self, client):
        try:
            result = client._api_handler.call(uri=self._page["previous"].replace(client._base_url, ''))
        except KeyError:
            raise exceptions.NotFound("There is no previous _page for this query")
        return PagedResult([Node(**temp_object) for temp_object in result["data"]], result["paging"])


class RankingType(Enum):
    """

    Representation of type of ranking
    * **All** - Top Anime Series
    * **Airing** - Top Airing Anime
    * **Upcoming** - Top Upcoming Anime
    * **TV** - Top TV Anime Series
    * **OVA** - Top OVA Anime Series
    * **Special** - Top Anime Specials
    * **Popular** - Top Anime by Popularity
    * **Favorite** - Top Favorited Anime
    """
    All = 'all'
    Airing = 'airing'
    Upcoming = 'upcoming'
    TV = 'tv'
    OVA = 'ova'
    Movie = 'movie'
    Special = 'special'
    Popular = 'bypopularity'
    Favorite = 'favorite'


class Sorting(Enum):
    """

    Representation of seasonal anime sorting
    * **Score** - Sorted by score
    * **User_Num** - Sorted by number of users in list
    """
    Score = "anime_score"
    User_Num = "anime_num_list_users"


class MyListSorting(Enum):
    """

    Sorting options for User Anime List
    * **ListScore** - Sorted by score given by user
    * **LastUpdate** - Sorted by most recently updated
    * **Title** - Sorted by title
    * **StartDate** - Sorted by broadcast start date
    * **Id** - Sorted by ID
    """
    ListScore = 'list_score'
    LastUpdate = 'list_updated_at'
    Title = "anime_title"
    StartDate =  "anime_start_date"
    Id = "anime_id"


class Rating(Enum):
    """

    Rating of shows provided by myanimelist:

    * **G** - All Ages
    * **PG** - Children
    * **PG_13** - Teens 13 and Older
    * **R** - 17+ (violence & profanity)
    * **RR** - Profanity & Mild Nudity
    * **Rx** - Hentai
    """
    G = 'g'
    PG = 'pg'
    PG_13 = 'pg_13'
    R = 'r'
    RR = 'r+'
    Rx = 'rx'


class Season(Enum):
    Winter = 'winter'
    Spring = 'spring'
    Summer = 'summer'
    Fall = 'fall'


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


class MyAnimeListStatus(MALBaseModel):
    """

    Status from users anime list

    """
    status: str
    score: int
    num_episodes_watched: int
    is_rewatching: bool
    updated_at: Union[datetime.datetime, str] #  Union[datetime.datetime, str].strptime(updated_at, '%Y-%m-%dT%H:%M:%S%z')


class AnimeType(Enum):
    """

    Enumerator representing anime type:

    * **Unknown**
    * **TV** - streamed in Japanese TV
    * **OVA** - Original Video Animation
    * **Movie** - animated movie
    * **Special** - special for anime
    * **ONA** - Original Net Anime
    * **Music** - music anime
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

    """
    Finished = 'finished_airing'
    Airing = 'currently_airing'
    Not_Yet_Aired = 'not_yet_aired'


class Source(Enum):
    """

    Enumerator representing source of anime

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

    """
    id: Optional[int]
    title: Optional[str]
    main_picture: Optional[Asset]
    alternative_titles: Optional[dict]
    start_date: Union[datetime.date, str, None] #  strptime(d['start_date'], '%Y-%m-%d').date()
    end_date: Union[datetime.date, str, None] #  strptime(d['end_date'], '%Y-%m-%d').date()
    synopsis: Optional[str]
    mean: Optional[float]
    rank: Optional[int]
    popularity: Optional[int]
    num_list_users: Optional[int]
    num_scoring_users: Optional[int]
    nsfw: Optional[Nsfw]
    genres: Union[list[Genre], None] #  There are series that have no genres on database, like this: 'Katsudou Shashin'
    created_at: Union[datetime.datetime, str, None] #  strptime(d['created_at'], '%Y-%m-%dT%H:%M:%S%z')
    updated_at: Union[datetime.datetime, str, None] #  strptime(d['updated_at'], '%Y-%m-%dT%H:%M:%S%z')
    media_type: Union[AnimeType, str, None]
    status: Optional[AnimeStatus]
    my_list_status: Optional[MyAnimeListStatus]
    num_episodes: Optional[int]
    start_season: Optional[AnimeSeason]
    broadcast: Optional[Broadcast]
    source: Optional[Union[Source, str]]
    average_episode_duration: Optional[int]
    rating: Optional[Rating]
    studios: Optional[list[Studio]]
    pictures: Optional[list[Asset]]
    background: Optional[str]
    related_anime: Optional[list[Relation]]
    related_manga: Optional[list[Relation]]
    recommendations: Optional[list[Recommendation]]

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.title


class MangaType(Enum):
    """

    Enumerator representing type of manga

    * **Unknown**
    * **Manga**
    * **Novel**
    * **One Shot**
    * **Doujinshi** - self-published manga
    * **Manhwa** - Korean comic
    * **Manhua** - Chinese comic
    * **OEL** - Original English-Language Manga
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
    Documentation says about loads more parameters but apparently only those are present

    """
    score: int
    status: str
    is_rereading: bool
    updated_at: Union[datetime.datetime, str] #  Union[datetime.datetime, str].strptime(updated_at, '%Y-%m-%dT%H:%M:%S%z')
    num_chapters_read: int
    num_volumes_read: int
    # TODO check for possible fields parameter manipulation
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

    """
    Finished = 'finished'
    Publishing = 'currently_publishing'
    Not_Yet_Published = 'not_yet_published'


class MangaObject(MALBaseModel):
    """

    Model of manga fetched from myanimelist

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
    media_type: Optional[MangaType, str]
    status: Optional[MangaStatus, str]
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


# Not used anywhere yet
class AnimeListStatus(MALBaseModel):
    """

    Status from users anime list

    """
    Node: Node
    score: int
    status: str
    is_rewatching: bool
    updated_at: Union[datetime.datetime, str]
    num_episodes_watched: int