from __future__ import annotations
from typing import Optional, Literal, Union

from .Datamodels import Fields, AnimeObject, Node, Season, PagedResult, AnimeRankingType, SeasonalAnimeSorting
from .exceptions import MainAuthRequiredError

__all__ = ["Anime"]


class Anime:
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
        params = {'fields': Fields.anime().to_payload()}
        data = self._api_handler.call(uri, params=params)
        return AnimeObject(**data)

    def get_anime_fields(self, id: int, fields: Fields) -> AnimeObject:
        """

        Get specific fields from MAL anime entry with provided id

        :param int id: id on https://myanimelist.net
        :param list[str] fields: list of string field names
        :returns: AnimeObject for requested id
        :rtype: AnimeObject
        """
        uri = f'anime/{id}'
        params = {'fields': fields.to_payload()}
        data = self._api_handler.call(uri, params=params)
        return AnimeObject(**data)

    def search_anime(self, keyword: str, *, limit: int = 20, nsfw: Optional[bool] = None, fields: Fields = Fields.node()) -> Union[PagedResult[Node], PagedResult[AnimeObject]]:
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
            'fields': fields.to_payload(),
            'nsfw': nsfw
        }
        temp = self._api_handler.call(uri=uri, params=params)
        r_class = Node if fields == Fields.node() else AnimeObject
        return PagedResult([r_class(**anime) for anime in temp["data"]], temp['paging'])

    def get_anime_ranking(self, *, ranking_type: Union[AnimeRankingType, str] = AnimeRankingType.ALL, fields: Fields = Fields.node(), limit: int = 50, offset: int = 0) -> Union[PagedResult[Node], PagedResult[AnimeObject]]:
        """
        Gets list of anime from MyAnimeList rankings

        :param Union[RankingType, str] ranking_type: [Optional] Name of ranking from which you want list to be fetched, default to Top Anime
        :param int limit: [Optional] Number of ranking entries to fetch, 50 by default
        :param int offset: [Optional] Position from which ranking fetch will start
        :return: List of entries fetched from MyAnimeList with paging support
        :rtype: PagedResult[None]
        """
        if isinstance(ranking_type, str):
            try:
                ranking_type = AnimeRankingType(ranking_type.lower())
            except ValueError:
                raise ValueError(f"ranking_type can't be '{ranking_type}'")
        uri = 'anime/ranking'
        params = {
            "ranking_type": ranking_type.value,
            "fields": fields.to_payload(),
            "limit": limit,
            'offset': offset,
        }
        temp = self._api_handler.call(uri=uri, params=params)
        r_class = Node if fields == Fields.node() else AnimeObject
        return PagedResult([r_class(**anime) for anime in temp["data"]], temp['paging'])

    SeasonT = Union[Season, Literal['winter', 'spring', 'summer', 'autumn']]

    def get_seasonal_anime(self, season: SeasonT, year: int, *, sort: Union[SeasonalAnimeSorting, str] = SeasonalAnimeSorting.SCORE, fields: Fields = Fields.anime(), limit: int = 50) -> Union[PagedResult[Node], PagedResult[AnimeObject]]:
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
                sort = SeasonalAnimeSorting(sort.lower())
            except ValueError:
                raise ValueError(f"sort can't be '{sort}'")

        if isinstance(season, str):
            try:
                season = Season(season.lower())
            except ValueError:
                raise ValueError(f"season can't be '{season}'")

        uri = f'anime/season/{year}/{season.value}'

        params = {
            "sort": sort.value.lower(),
            "limit": limit,
            "fields": fields.to_payload(),
        }
        temp = self._api_handler.call(uri=uri, params=params)
        r_class = Node if fields == Fields.node() else AnimeObject
        return PagedResult([r_class(**anime) for anime in temp["data"]], temp['paging'])

    def get_suggested_anime(self, *, fields: Fields = Fields.node(), limit: int = 20, offset: int = 0) -> Union[PagedResult[Node], PagedResult[AnimeObject]]:
        """
        Gets list of suggested anime suggested for user

        :return: List of entries fetched from MyAnimeList with paging support
        :rtype: PagedResult[None]
        """
        if not self.authorized:
            raise MainAuthRequiredError()
        uri = 'anime/suggestions'
        params = {"limit": limit,
                  "offset": offset,
                  "fields": fields.to_payload()}

        temp = self._api_handler.call(uri=uri, params=params)
        r_class = Node if fields == Fields.node() else AnimeObject
        return PagedResult([r_class(**anime) for anime in temp["data"]], temp['paging'])
