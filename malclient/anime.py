from typing import Optional, Literal

from .models import AnimeObject, Node, Season

# Fields that will be requested from myanimelist server by default
__anime_fields__ = [
            "id",
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
            "average_episode_duration"
            "rating",
            "pictures",
            "background",
            "related_anime",
            "related_manga",
            "recommendations",
            "studios"]


class Anime():
    def __init__(self):
        return

    def get_anime_details(self, id: int) -> AnimeObject:
        """
        Get full info about anime with provided id

        :param id: id on https://myanimelist.net

        :returns: AnimeObject for requested id
        """
        id = str(id)
        uri = f'anime/{id}'
        params = {'fields': ','.join(__anime_fields__), }
        data = self._api_handler.call(uri, params=params)
        return AnimeObject(**data)

    # TODO need pagination here
    #  anime_fields misses usage
    def search_anime(self, keyword: str, *, limit: int = 20, nsfw: Optional[bool] = None, anime_fields=None) -> list[Node]:
        """
        Lookup anime with keyword phrase on https://myanimelist.net

        :param keyword: string to look by
        :param limit: number of queries returned
        :param nsfw: boolean enabling/disabling nsfw filter

        :returns: list of anime Node objects
        """
        if nsfw is None:
            nsfw = self.nsfw
        uri = 'anime'
        params = {
            "q": keyword,
            'limit': limit,
            'fields': ','.join(__anime_fields__),
            'nsfw': nsfw
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return [Node(**temp_object) for temp_object in temp]

    # TODO objectify anime ranking
    def get_anime_ranking(self, ranking_type: str = "all", limit: int = 20) -> dict:
        uri = 'anime/ranking'
        ranking_types = [
            "all", "airing", "upcoming", "tv", "ova", "movie", "special",
            "bypopularity", "favorite"
        ]
        if ranking_type not in ranking_types:
            return
        params = {
            "ranking_type": ranking_types,
            "fields": ','.join(self.anime_fields),
            "limit": limit
        }
        return self._api_handler.call(uri=uri, params=params)

    # TODO objectify seasonal anime
    def get_seasonal_anime(self, season: Season, sort: Literal["anime_score", "anime_num_list_users"] = "anime_score", limit: int = 20) -> dict:

        sort_options = ["anime_score", "anime_num_list_users"]
        if sort.lower() not in sort_options:
            raise AttributeError('Sort must be "anime_score" or "anime_num_list_users"')
        uri = f'anime/season/{season.year}/{season.season}'

        params = {
            "sort": sort.lower(),
            "limit": limit,
            "fields": ','.join(self.anime_fields)
        }
        return self._api_handler.call(uri=uri, params=params)

    # TODO objectify suggested anime
    def get_suggested_anime(self, limit: int = 20):
        uri = 'anime/suggestions'
        params = {"limit": limit}
        return self._api_handler.call(uri=uri, params=params)
