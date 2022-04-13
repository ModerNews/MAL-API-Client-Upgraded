from typing import Optional, Literal, Union, List

from .models import AnimeObject, Node, Season, PagedResult, RankingType, Sorting

__node_fields__ = ['id',
                   'title',
                   'main_picture']

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

        :param int id: id on https://myanimelist.net
        :returns: AnimeObject for requested id
        :rtype: AnimeObject
        """
        id = str(id)
        uri = f'anime/{id}'
        params = {'fields': ','.join(__anime_fields__), }
        data = self._api_handler.call(uri, params=params)
        return AnimeObject(**data)

    # TODO anime_fields misses usage
    def search_anime(self, keyword: str, *, limit: int = 20, nsfw: Optional[bool] = None, anime_fields=None) -> PagedResult[Node]:
        """
        Lookup anime with keyword phrase on https://myanimelist.net

        :param str keyword: string to look by
        :param int limit: number of queries returned
        :param bool nsfw: boolean enabling/disabling nsfw filter
        :returns: list of anime Node objects
        :rtype: list[Node]
        """
        if nsfw is None:
            nsfw = self.nsfw
        uri = 'anime'
        params = {
            "q": keyword,
            'limit': limit,
            'fields': ','.join(__node_fields__),
            'nsfw': nsfw
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult([Node(**temp_object) for temp_object in temp["data"]], temp["paging"])

    def get_anime_ranking(self, *, ranking_type: Union[RankingType, str] = RankingType.All, limit: int = 50) -> PagedResult[Node]:
        """
        Gets list of anime from MyAnimeList rankings

        :param Union[RankingType, str] ranking_type: [Optional] Name of ranking from which you want list to be fetched, default to Top Anime
        :param int limit: [Optional] Number of ranking entries to fetch, 50 by default
        :return: List of entries fetched from MyAnimeList with paging support
        :rtype: PagedResult[None]
        """
        if isinstance(ranking_type, str):
            try:
                RankingType(ranking_type.lower())
            except:
                raise ValueError(f"ranking_type can't be '{ranking_type}'")
        uri = 'anime/ranking'
        params = {
            "ranking_type": ranking_type.value,
            "fields": ','.join(__node_fields__),
            "limit": limit
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult([Node(**anime) for anime in temp["data"]], temp["paging"])

    SeasonT = Union[Season, Literal['winter', 'spring', 'summer', 'autumn']]

    def get_seasonal_anime(self, season: SeasonT, year: int, *, sort: Union[Sorting, str] = Sorting.Score, limit: int = 50) -> PagedResult[Node]:
        """
        Gets list of anime from specified season

        :param SeasonT season: Season of year to fetch
        :param int year: Year to fetch
        :param Union[Sorting, str] sort: Sorting method for query, default to Score
        :param int limit: [Optional] Number of series to fetch, 50 by default
        :return: List of entries fetched from MyAnimeList with paging support
        :rtype: PagedResult[None]
        """
        if isinstance(sort, str):
            try:
                Sorting(sort.lower())
            except:
                raise ValueError(f"sort can't be '{sort}'")

        if isinstance(season, str):
            try:
                Season(season.lower())
            except:
                raise ValueError(f"season can't be '{season}'")

        sort_options = ["anime_score", "anime_num_list_users"]
        if sort.lower() not in sort_options:
            raise AttributeError('Sort must be "anime_score" or "anime_num_list_users"')
        uri = f'anime/season/{year}/{season.season}'

        params = {
            "sort": sort.lower(),
            "limit": limit,
            "fields": ','.join(__anime_fields__)
        }
        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult(temp['data'], temp['paging'])

    def get_suggested_anime(self, limit: int = 20) -> PagedResult[Node]:
        """
        Gets list of suggested anime suggested for user

        :return: List of entries fetched from MyAnimeList with paging support
        :rtype: PagedResult[None]
        """
        uri = 'anime/suggestions'
        params = {"limit": limit}

        temp = self._api_handler.call(uri=uri, params=params)
        return PagedResult(temp['data'], temp['paging'])
