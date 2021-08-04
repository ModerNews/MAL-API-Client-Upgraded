import datetime
from enum import Enum


class Genre(object):
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id


# class MediaType(Enum):
#     TV = 'tv'
#     ONA = 'ona'
#     OVA = 'ova'
#     Movie = 'movie'
#     SPECIAL = 'special'
#
#     def __repr__(self):


class Node(object):
    def __init__(self, id, title, main_picture):
        self.id: int = id
        self.title: str = title
        self.main_picture: dict[str, str] = main_picture

    def __eq__(self, other):
        return self.id == other.id


class Relation(object):
    def __init__(self, node, relation_type, relation_type_formatted):
        self.node: Node = node
        self.relation_type: str = relation_type
        self.relation_type_formatted: str = relation_type_formatted


class AnimeListStatus(object):
    def __init__(self, id, title, main_picture, score, status, num_episodes_watched, is_rewatching, updated_at, start_date, finish_date):
        self.id: int = id
        self.title: str = title
        self.main_picture: dict[str, str] = main_picture
        self.score: int = score
        self.status: str = status
        self.is_rewatching: bool = is_rewatching
        self.updated_at: datetime.datetime = datetime.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S%z')
        self.num_episodes_watched: int = num_episodes_watched
        self.start_date: datetime.date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.finish_date: datetime.date = datetime.datetime.strptime(finish_date, '%Y-%m-%d').date()


class Recommendation(object):
    def __init__(self, id, title, main_picture, num_recomendations):
        self.num_recomendations: int = num_recomendations
        self.node: Node = Node(id, title, main_picture)


class Season(object):
    def __init__(self, year, season):
        self.year: int = year
        self.season: str = season

    def __str__(self):
        return f'{self.season} {self.year}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.year == other.year and self.season == other.season


class Studio(object):
    def __init__(self, id, name):
        self.id: int = id
        self.name = name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id


class AnimeObject(object):
    def __init__(self, d):
        self.d: dict = d
        self.id: int = d['id']
        self.title: str = d['title']
        self.alternative_titles: dict[str, str] = d['alternative_titles']
        self.synopsis: str = d['synopsis']
        self.background: str = d['background']
        self.broadcast: dict[str, str] = d['broadcast']
        self.created_at: datetime.datetime = datetime.datetime.strptime(d['created_at'], '%Y-%m-%dT%H:%M:%S%z')
        self.start_date: datetime.date = datetime.datetime.strptime(d['start_date'], '%Y-%m-%d').date()
        self.end_date: datetime.date = datetime.datetime.strptime(d['end_date'], '%Y-%m-%d').date()
        self.genres: list[Genre] = [Genre(temp['id'], temp['name']) for temp in d['genres']]
        # TODO create Image object
        self.main_picture: dict[str, str] = d['main_picture']
        # fixed set of values
        self.media_type: str = d['media_type']
        self.mean: int = d['mean']
        self.my_list_status: AnimeListStatus = AnimeListStatus(self.id, self.title, self.main_picture, d['my_list_status']['score'], d['my_list_status']['status'], d['my_list_status']['num_episodes_watched'], d['my_list_status']['is_rewatching'], d['my_list_status']['updated_at'], d['my_list_status']['start_date'], d['my_list_status']['finish_date'])
        # fixed set of values
        self.nsfw: str = d['nsfw']
        self.num_episodes: int = d['num_episodes']
        self.num_list_users: int = d['num_list_users']
        self.num_scoring_users: int = d['num_scoring_users']
        self.popularity: int = d['popularity']
        self.rank: int = d['rank']
        self.recomendations: list[Recommendation] = [Recommendation(temp_recomendation['node']['id'], temp_recomendation['node']['title'], temp_recomendation['node']['main_picture'], temp_recomendation['num_recommendations']) for temp_recomendation in d['recommendations']]
        self.related_anime: list[Relation] = [Relation(Node(temp_relation['node']['id'], temp_relation['node']['title'], temp_relation['node']['main_picture']), temp_relation['relation_type'], temp_relation['relation_type_formatted']) for temp_relation in d['related_anime']]
        self.related_manga: list[Relation] = [Relation(Node(temp_relation['node']['id'], temp_relation['node']['title'], temp_relation['node']['main_picture']), temp_relation['relation_type'], temp_relation['relation_type_formatted']) for temp_relation in d['related_manga']]
        self.source: str = d['source']
        self.start_season: Season = Season(d['start_season']['year'], d['start_season']['season'])
        self.status: str = d['status']
        self.studios: list[Studio] = [Studio(temp_studio['id'], temp_studio['name']) for temp_studio in d['studios']]
        self.updated_at: datetime.datetime = datetime.datetime.strptime(d['updated_at'], '%Y-%m-%dT%H:%M:%S%z')

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.title