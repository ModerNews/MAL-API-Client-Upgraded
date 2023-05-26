from types import MethodType, MethodWrapperType, BuiltinFunctionType
from typing import Union

__all__ = ['Fields', 'AuthorFields', 'ListStatusFields', 'UserFields', "CharacterFields"]


class FieldsBase(object):
    """
    Base class for all Field classes
    """
    def __init__(self, **kwargs):
        pass

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            for field in dir(self):
                if type(self.__getattribute__(field)) not in (MethodType, MethodWrapperType, BuiltinFunctionType):
                    if self.__getattribute__(field) != other.__getattribute__(field):
                        return False
                else:
                    continue
        return True

    def __repr__(self):
        """
        Returns string representation of dictionary containing all Fields
        """
        return str(self.__dict__)

    def to_payload(self):
        """
        Generates query string for fields parameter
        """
        fields = []
        for field, value in self.__dict__.items():
            if isinstance(value, FieldsBase):
                if value == value.empty():
                    continue
                else:
                    fields.append(field[1:] + '{' + str(",".join([key for key, state in value.__dict__.items() if state])) + '}')
            elif value is True:
                fields.append(field)
        return ','.join(fields)

    def _generate_subclass(self, r_type, value):
        return r_type(**value) if isinstance(value, dict) else value if isinstance(
            value, r_type) else False if value is not True else r_type()

    @classmethod
    def from_list(cls, field_list: list[str]):
        """
        Generates fields object based of list of fields
        """
        return cls(**{field: True for field in field_list})

    @classmethod
    def all(cls):
        """
        Generates fields object containing all fields possible
        """
        return cls.from_list(dir(cls()))

    @classmethod
    def empty(cls):
        """
        Generates empty fields object
        Might be overridden by some classes, which have parameters set to True by default
        """
        return cls()


class Fields(FieldsBase):
    """
    Object containing all fields possible for anime and manga
    num_favorites, opening_themes, ending_themes are not documented by MAL
    """
    def __init__(self, **kwargs):
        # general
        self.id: bool = kwargs.get('id', True)
        self.title: bool = kwargs.get('title', True)
        self.main_picture: bool = kwargs.get('main_picture', True)
        self.alternative_titles: bool = kwargs.get('alternative_titles', False)
        self.start_date: bool = kwargs.get('start_date', False)
        self.end_date: bool = kwargs.get('end_date', False)
        self.synopsis: bool = kwargs.get('synopsis', False)
        self.mean: bool = kwargs.get('mean', False)
        self.rank: bool = kwargs.get('rank', False)
        self.popularity: bool = kwargs.get('popularity', False)
        self.num_list_users: bool = kwargs.get('num_list_users', False)
        self.num_scoring_users: bool = kwargs.get('num_scoring_users', False)
        self.updated_at: bool = kwargs.get('updated_at', False)
        self.genres: bool = kwargs.get('genres', False)
        # self.my_list_status: bool = kwargs.get('my_list_status', False)
        self._my_list_status: ListStatusFields = self._generate_subclass(ListStatusFields, kwargs.get('my_list_status', False))
        self.pictures: bool = kwargs.get('pictures', False)
        self.background: bool = kwargs.get('background', False)
        self._related_anime: bool = self._generate_subclass(Fields, kwargs.get('related_anime', False))
        self._related_manga: bool = self._generate_subclass(Fields, kwargs.get('related_manga', False))
        self._recommendations: bool = self._generate_subclass(Fields, kwargs.get('recommendations', False))
        self.nsfw: bool = kwargs.get('nsfw', False)
        self.created_at: bool = kwargs.get('created_at', False)
        self.media_type: bool = kwargs.get('media_type', False)
        self.status: bool = kwargs.get('status', False)
        self.num_favorites: bool = kwargs.get('num_favorites', False)

        # anime related
        self.num_episodes: bool = kwargs.get('num_episodes', False)
        self.start_season: bool = kwargs.get('start_season', False)
        self.broadcast: bool = kwargs.get('broadcast', False)
        self.source: bool = kwargs.get('source', False)
        self.average_episode_duration: bool = kwargs.get('average_episode_duration', False)
        self.rating: bool = kwargs.get('rating', False)
        self.studios: bool = kwargs.get('studios', False)
        self.opening_themes: bool = kwargs.get('opening_themes', False)
        self.ending_themes: bool = kwargs.get('ending_themes', False)
        self.statistics: bool = kwargs.get('statistics', False)
        self.videos: bool = kwargs.get('videos', False)

        # manga related
        self.num_volumes: bool = kwargs.get('num_volumes', False)
        self.num_chapters: bool = kwargs.get('num_chapters', False)
        self._authors: Union[AuthorFields, bool] = self._generate_subclass(AuthorFields, kwargs.get('authors', False))
        self.serialization: bool = kwargs.get('serialization', False)

        # endpoint specific
        self._list_status: Union[ListStatusFields, bool] = self._generate_subclass(ListStatusFields, kwargs.get('list_status'))
        # self._list_status: bool = kwargs.get('ranking', False)

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        self._authors = self._generate_subclass(AuthorFields, value)

    @property
    def list_status(self):
        return self._list_status

    @list_status.setter
    def list_status(self, value):
        self._list_status = self._generate_subclass(ListStatusFields, value)

    @property
    def related_anime(self):
        return self._related_anime

    @related_anime.setter
    def related_anime(self, value):
        self._related_anime = self._generate_subclass(Fields, value)

    @property
    def related_manga(self):
        return self._related_manga

    @related_manga.setter
    def related_manga(self, value):
        self._related_manga = self._generate_subclass(Fields, value)

    @property
    def recommendations(self):
        return self._recommendations

    @recommendations.setter
    def recommendations(self, value):
        self._recommendations = self._generate_subclass(Fields, value)

    @property
    def my_list_status(self):
        return self._my_list_status

    @my_list_status.setter
    def my_list_status(self, value):
        self._my_list_status: ListStatusFields = self._generate_subclass(ListStatusFields, value)

    @classmethod
    def empty(cls):
        return cls(id=False, title=False, main_picture=False)

    @classmethod
    def node(cls):
        """
        Generates Fields object containing only parameters taken by node
        """
        return cls().from_list(['id', 'title', 'main_picture'])

    @classmethod
    def anime(cls):
        """
        Generates Fields object containing all parameters taken by anime
        """
        return cls().from_list(["id",
                                "title",
                                "main_picture",
                                "alternative_titles",
                                "start_date",
                                "end_date",
                                "synopsis",
                                "mean",
                                "rank",
                                "popularity",
                                "num_list_users",
                                "num_scoring_users",
                                "nsfw",
                                "created_at",
                                "updated_at",
                                "media_type",
                                "status",
                                "genres",
                                "my_list_status",
                                "num_episodes",
                                "start_season",
                                "broadcast",
                                "source",
                                "average_episode_duration",
                                "rating",
                                "pictures",
                                "background",
                                "related_anime",
                                "related_manga",
                                "recommendations",
                                "studios",
                                "opening_theme",
                                'ending_theme',
                                'videos',])

    @classmethod
    def manga(cls):
        """
        Generates Fields object containing all parameters taken by manga
        """
        return cls(id=True,
                   title=True,
                   main_picture=True,
                   alternative_titles=True,
                   start_date=True,
                   end_date=True,
                   synopsis=True,
                   mean=True,
                   rank=True,
                   popularity=True,
                   num_list_users=True,
                   num_scoring_users=True,
                   nsfw=True,
                   created_at=True,
                   updated_at=True,
                   media_type=True,
                   status=True,
                   genres=True,
                   my_list_status=True,
                   num_volumes=True,
                   num_chapters=True,
                   authors=True,
                   pictures=True,
                   background=True,
                   related_anime=True,
                   related_manga=True,
                   recommendations=True,
                   serialization=True)


# class RecursiveFieldFields(Fields):
#
#
#
class AuthorFields(FieldsBase):
    """
    Helper fields class containing info about manga author
    """
    def __init__(self, **kwargs):
        self.first_name: bool = kwargs.get('first_name', True)
        self.last_name: bool = kwargs.get('last_name', True)

    @classmethod
    def empty(cls):
        return cls(first_name=False, last_name=False)


class ListStatusFields(FieldsBase):
    """
    Helper fields class containing precise data for my_list_status
    """
    def __init__(self, **kwargs):
        self.priority: bool = kwargs.get('priority', False)
        self.tags: bool = kwargs.get('tags', False)
        self.comments: bool = kwargs.get('comments', False)

        self.num_times_reread: bool = kwargs.get('num_times_reread', False)
        self.reread_value: bool = kwargs.get('reread_value', False)

        self.num_times_rewatched: bool = kwargs.get('num_times_rewatched', False)
        self.rewatch_value: bool = kwargs.get('rewatch_value', False)

        # DEPRECATED FIELDS - Always present in request
        # self.score: bool = kwargs.get('score', True)
        # self.status: bool = kwargs.get('status', True)
        # self.updated_at: bool = kwargs.get('updated_at', True)
        # self.start_date: bool = kwargs.get('start_date', False)
        # self.finish_date: bool = kwargs.get('finish_date', False)
        # self.is_rereading: bool = kwargs.get('is_rereading', False)
        # self.num_chapters_read: bool = kwargs.get('num_chapters_read', False)
        # self.num_volumes_read: bool = kwargs.get('num_volumes_read', False)
        # self.num_episodes_watched: bool = kwargs.get('num_episodes_watched', False)
        # self.is_rewatching: bool = kwargs.get('is_rewatching', False)

    @classmethod
    def empty(cls):
        return cls(score=False, status=False, updated_at=False)


    @classmethod
    def manga_full(cls):
        """
        All fields for manga list status
        """
        return cls.from_list(['priority', 'tags', 'comments', 'num_times_reread', 'reread_value'])

    @classmethod
    def anime_full(cls):
        """
        All fields for anime list status
        """
        return cls.from_list(['priority', 'tags', 'comments', 'num_times_rewatched', 'rewatch_value'])


class UserFields(FieldsBase):
    def __init__(self, **kwargs):
        self.id: bool = kwargs.get("id", True)
        self.name: bool = kwargs.get("name", True)
        self.picture: bool = kwargs.get("picture", True)
        self.gender: bool = kwargs.get("gender", True)
        self.birthday: bool = kwargs.get("birthday", False)
        self.location: bool = kwargs.get("location", True)
        self.joined_at: bool = kwargs.get("joined_at", True)
        self.anime_statistics: bool = kwargs.get("anime_statistics", True)
        self.time_zone: bool = kwargs.get("time_zone", False)
        self.is_supporter: bool = kwargs.get("is_supporter", False)

    @classmethod
    def basic(cls):
        return cls(id=True,
                   name=True,
                   picture=True,
                   anime_statistics=True)


class CharacterFields(FieldsBase):
    def __init__(self, **kwargs):
        self.id: bool = kwargs.get("id", True)
        self.role: bool = kwargs.get("role", True)
        self.first_name: bool = kwargs.get("first_name", False)
        self.last_name: bool = kwargs.get("last_name", False)
        self.alternative_name: bool = kwargs.get("alternative_name", False)
        self.main_picture: bool = kwargs.get("main_picture", False)
        self.biography: bool = kwargs.get("biography", False)
        self.pictures: bool = kwargs.get("pictures", False)
        self._animeography: Fields = self._generate_subclass(Fields, kwargs.get("animeography", False))
        self.num_favorites: bool = kwargs.get("num_favorites", False)

    @property
    def animeography(self) -> Fields:
        return self._animeography

    @animeography.setter
    def animeography(self, value: Fields):
        self._animeography: Fields = self._generate_subclass(Fields, value)


# Deprecated - This serves no purpose, you can't specify fields for this parameter
# class AnimeStatisticsFields(FieldsBase):
#     def __init__(self, **kwargs):
#         self.num_items_watching: bool = kwargs.get("num_items_watching", False)
#         self.num_items_completed: bool = kwargs.get("num_items_completed", False)
#         self.num_items_on_hold: bool = kwargs.get("num_items_on_hold", False)
#         self.num_items_dropped: bool = kwargs.get("num_items_dropped", False)
#         self.num_items_plan_to_watch: bool = kwargs.get("num_items_plan_to_watch", False)
#         self.num_items: bool = kwargs.get("num_items", False)
#         self.num_days_watched: bool = kwargs.get("num_days_watched", False)
#         self.num_days_watching: bool = kwargs.get("num_days_watching", False)
#         self.num_days_completed: bool = kwargs.get("num_days_completed", False)
#         self.num_days_on_hold: bool = kwargs.get("num_days_on_hold", False)
#         self.num_days_dropped: bool = kwargs.get("num_days_dropped", False)
#         self.num_days: bool = kwargs.get("num_days", False)
#         self.num_episodes: bool = kwargs.get("num_episodes", False)
#         self.num_times_rewatched: bool = kwargs.get("num_times_rewatched", False)
#         self.mean_score: bool = kwargs.get("mean_score", False)
