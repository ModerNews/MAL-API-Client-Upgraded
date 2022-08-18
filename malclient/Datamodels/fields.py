from types import MethodType, MethodWrapperType, BuiltinFunctionType
from typing import Union

__all__ = ['Fields', 'AuthorFields', 'ListStatusFields']


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
        self.my_list_status: bool = kwargs.get('my_list_status', False)
        self.pictures: bool = kwargs.get('pictures', False)
        self.background: bool = kwargs.get('background', False)
        self._related_anime: bool = self._generate_subclass(Fields, kwargs, 'related_anime')
        self._related_manga: bool = self._generate_subclass(Fields, kwargs, 'related_manga')
        self._recommendations: bool = self._generate_subclass(Fields, kwargs, 'recommendations')
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
        self.opening_themes: bool = kwargs.get('opening_theme', False)
        self.ending_themes: bool = kwargs.get('ending_theme', False)
        self.statistics: bool = kwargs.get('statistics', False)

        # manga related
        self.num_volumes: bool = kwargs.get('num_volumes', False)
        self.num_chapters: bool = kwargs.get('num_chapters', False)
        self._authors: Union[AuthorFields, bool] = self._generate_subclass(AuthorFields, kwargs, 'authors')
        self.serialization: bool = kwargs.get('serialization', False)

    def _generate_subclass(self, r_type, kwargs, key):
        return r_type(**kwargs.get(key)) if isinstance(kwargs.get(key), dict) else kwargs.get(key) if isinstance(kwargs.get(key), r_type) else False if kwargs.get(key) is not True else r_type()

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        self._authors = self._generate_subclass(AuthorFields, {'authors': value}, 'authors')

    @property
    def related_anime(self):
        return self._related_anime

    @related_anime.setter
    def related_anime(self, value):
        self._related_anime = self._generate_subclass(Fields, {'related_anime': value}, 'related_anime')

    @property
    def related_manga(self):
        return self._related_manga

    @related_manga.setter
    def related_manga(self, value):
        self._related_manga = self._generate_subclass(Fields, {'related_manga': value}, 'related_manga')

    @property
    def recommendations(self):
        return self._recommendations

    @recommendations.setter
    def recommendations(self, value):
        self._recommendations = self._generate_subclass(Fields, {'recommendations': value}, 'recommendations')

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
                                'ending_theme', ])

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
        self.score: bool = kwargs.get('score', True)
        self.status: bool = kwargs.get('status', True)
        self.updated_at: bool = kwargs.get('updated_at', True)
        self.start_date: bool = kwargs.get('start_date', False)
        self.finish_date: bool = kwargs.get('finish_date', False)
        self.priority: bool = kwargs.get('priority', False)
        self.tags: bool = kwargs.get('tags', False)
        self.comments: bool = kwargs.get('comments', False)

        # manga only
        self.is_rereading: bool = kwargs.get('is_rereading', False)
        self.num_chapters_read: bool = kwargs.get('num_chapters_read', False)
        self.num_volumes_read: bool = kwargs.get('num_volumes_read', False)
        self.num_times_reread: bool = kwargs.get('num_times_reread', False)
        self.reread_value: bool = kwargs.get('reread_value', False)

        # anime only
        self.num_episodes_watched: bool = kwargs.get('num_episodes_watched', False)
        self.is_rewatching: bool = kwargs.get('is_rewatching', False)
        self.num_times_rewatched: bool = kwargs.get('num_times_rewatched', False)
        self.rewatch_value: bool = kwargs.get('rewatch_value', False)

    @classmethod
    def empty(cls):
        return cls(score=False, status=False, updated_at=False)

    @classmethod
    def manga_base(cls):
        """
        Base fields for manga list status
        """
        return cls.from_list(['score', 'status', 'updated_at', 'is_rereading', 'num_chapters_read', 'num_volumes_read', 'start_date', 'finish_date'])

    @classmethod
    def manga_full(cls):
        """
        All fields for manga list status
        """
        return cls.from_list(['score', 'status', 'updated_at', 'is_rereading', 'num_chapters_read', 'num_volumes_read', 'start_date', 'finish_date', 'priority', 'tags', 'comments', 'num_times_reread', 'reread_value'])

    @classmethod
    def anime_base(cls):
        """
        Base fields for anime list status
        """
        return cls.from_list(['score', 'status', 'updated_at', 'is_rewatching', 'num_episodes_watched'])

    @classmethod
    def anime_full(cls):
        """
        All fields for anime list status
        """
        return cls.from_list(['score', 'status', 'updated_at', 'is_rewatching', 'num_episodes_watched', 'priority', 'tags', 'comments', 'num_times_rewatched', 'rewatch_value'])
