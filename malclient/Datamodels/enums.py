from __future__ import annotations
from enum import Enum

__all__ = ['Nsfw', 'RelationType', 'Rating', 'Season', 'AnimeType', 'AnimeStatus', 'AnimeSource', 'MangaType',
           'MangaStatus', 'MangaRankingType', 'AnimeRankingType', 'SeasonalAnimeSorting', "MyAnimeListSorting",
           "MyMangaListSorting"]


class Nsfw(Enum):
    """

    Enumerator representing nsfw stages:

    """
    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class RelationType(Enum):
    """

    Enumerator representing possible relation types between anime and/or manga:

    """
    SEQUEL = "sequel"
    PREQUEL = "prequel"
    ALT_SETTING = "alternative_setting"
    ALT_VERSION = "alternative_version"
    SIDE_STORY = "side_story"
    PARENT_STORY = "parent_story"
    SUMMARY = "summary"
    FULL_STORY = "full_story"
    SPIN_OFF = 'spin_off'
    CHARACTER = 'character'
    OTHER = 'other'


class AnimeRankingType(Enum):
    """

    Representation of possible values for anime ranking type
    * **ALL** - Top Anime Series
    * **AIRING** - Top Airing Anime
    * **UPCOMING** - Top Upcoming Anime
    * **TV** - Top TV Anime Series
    * **OVA** - Top OVA Anime Series
    * **MOVIE** - Top Anime Movies
    * **SPECIAL** - Top Anime Specials
    * **POPULAR** - Top Anime by Popularity
    * **FAVORITE** - Top Favorite Anime
    """
    ALL = 'all'
    AIRING = 'airing'
    UPCOMING = 'upcoming'
    TV = 'tv'
    OVA = 'ova'
    MOVIE = 'movie'
    SPECIAL = 'special'
    POPULAR = 'bypopularity'
    FAVORITE = 'favorite'


class MangaRankingType(Enum):
    """

    Representation of possible values for manga ranking type
    * **ALL** - All
    * **MANGA** - Top Manga
    * **NOVELS** - Top Novels
    * **ONE_SHOTS** - Top One Shot Manga
    * **DOUJIN** - Top Doujinshi
    * **MANHWA** - Top Manhwa
    * **MANHUA** - Top Manhua
    * **POPULAR** - Most popular
    * **FAVORITE** - Most Favorited
    """
    ALL = 'all'
    MANGA = 'manga'
    NOVELS = 'novels'
    ONE_SHOTS = 'oneshots'
    DOUJIN = 'doujin'
    MANHWA = 'manhwa'
    MANHUA = 'manhua'
    POPULAR = 'bypopularity'
    FAVORITE = 'favorite'


class SeasonalAnimeSorting(Enum):
    """

    Representation of seasonal anime sorting
    * **SCORE** - Sorted by score
    * **USER_NUM** - Sorted by number of users in list
    """
    SCORE = "anime_score"
    USER_NUM = "anime_num_list_users"


class MyAnimeListSorting(Enum):
    """

    Sorting options for User Anime List
    * **LIST_SCORE** - Sorted by score given by user
    * **LAST_UPDATE** - Sorted by most recently updated
    * **TITLE** - Sorted by title
    * **START_DATE** - Sorted by broadcast start date
    * **ID** - Sorted by ID
    """
    LIST_SCORE = 'list_score'
    LAST_UPDATE = 'list_updated_at'
    TITLE = "anime_title"
    START_DATE = "anime_start_date"
    ID = "anime_id"


class MyMangaListSorting(Enum):
    """

    Sorting options for User Manga List
    * **LIST_SCORE** - Sorted by score given by user
    * **LAST_UPDATE** - Sorted by most recently updated
    * **TITLE** - Sorted by title
    * **START_DATE** - Sorted by series start date
    * **ID** - Sorted by manga ID
    """
    LIST_SCORE = 'list_score'
    LAST_UPDATE = 'list_updated_at'
    TITLE = "manga_title"
    START_DATE = "manga_start_date"
    ID = "manga_id"


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
    WINTER = 'winter'
    SPRING = 'spring'
    SUMMER = 'summer'
    FALL = 'fall'


class AnimeStatus(Enum):
    """

    Enumerating representing current anime status

    """
    FINISHED = 'finished_airing'
    AIRING = 'currently_airing'
    NOT_AIRED = 'not_yet_aired'


class MangaStatus(Enum):
    """

    Enumerating representing current manga status

    """
    FINISHED = 'finished'
    PUBLISHING = 'currently_publishing'
    NOT_PUBLISHED = 'not_yet_published'


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
    UNKNOWN = "unknown"
    TV = "tv"
    OVA = 'ova'
    MOVIE = 'movie'
    SPECIAL = 'special'
    ONA = 'ona'
    MUSIC = 'Music'


class MangaType(Enum):
    """

    Enumerator representing type of manga

    * **UNKNOWN**
    * **MANGA**
    * **NOVEL**
    * **ONE_SHOT**
    * **DOUJIN** - self-published manga
    * **MANHWA** - Korean comic
    * **MANHUA** - Chinese comic
    * **OEL** - Original English-Language Manga
    """
    UNKNOWN = "unknown"
    MANGA = "manga"
    NOVEL = "novel"
    ONE_SHOT = "one_shot"
    DOUJIN = "doujinshi"
    MANHWA = "manhwa"
    MANHUA = "manhua"
    OEL = "oel"


class AnimeSource(Enum):
    """

    Enumerator representing source of anime

    """
    OTHER = "other"
    ORIGINAL = "original"
    MANGA = "manga"
    MANGA_4_KOMA = "4_koma_manga"
    WEB_MANGA = "web_manga"
    DIGITAL_MANGA = "digital_manga"
    NOVEL = "novel"
    LIGHT_NOVEL = "light_novel"
    VISUAL_NOVEL = "visual_novel"
    GAME = "game"
    CARD_GAME = "card_game"
    BOOK = "book"
    PICTURE_BOOK = "picture_book"
    RADIO = "radio"
    MUSIC = "music"
