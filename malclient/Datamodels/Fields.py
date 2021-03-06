from types import MethodType, MethodWrapperType, BuiltinFunctionType

__all__ = ['Fields', 'AuthorFields']


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
                    fields.append('authors{' + str(",".join([key for key, state in value.__dict__.items() if state])) + '}')
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
        Might be overriden by some classes, which have parameters set to True by default
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
        self.main_picture: bool = kwargs.get('main_picture', False)
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
        self.related_anime: bool = kwargs.get('related_anime', False)
        self.related_manga: bool = kwargs.get('related_manga', False)
        self.recommendations: bool = kwargs.get('recommendations', False)
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
        self.authors: AuthorFields = AuthorFields(**kwargs.get('authors')) if isinstance(kwargs.get('authors'), dict) else kwargs.get('authors') if isinstance(kwargs.get('authors'), AuthorFields) else AuthorFields.empty() if kwargs.get('authors') is not True else AuthorFields.all()
        self.serialization: bool = kwargs.get('serialization', False)

    @classmethod
    def empty(cls):
        return cls(id=False, title=False)

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
                                'ending_theme',])

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


class AuthorFields(FieldsBase):
    """
    Helper fields class containing info about manga author
    """
    def __init__(self, **kwargs):
        self.first_name: bool = kwargs.get('first_name', False)
        self.last_name: bool = kwargs.get('last_name', False)

    @classmethod
    def empty(cls):
        return cls(first_name=False, last_name=False)
