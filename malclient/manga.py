from __future__ import annotations

from typing import Union

from .Datamodels import MangaObject, Node, Fields, PagedResult, MangaRankingType

__all__ = ["Manga"]


class Manga:
    def __init__(self):
        return

    def search_manga(self, keyword: str, fields: Fields = Fields.node(), limit: int = 20, offset: int = 0, nsfw: bool = None) -> list[Node]:
        """
        Lookup manga with keyword phrase on https://myanimelist.net

        :param str keyword: string to look by
        :param Fields fields: fields that will be returned by API in addition to default ones
        :param int limit: number of queries returned
        :param int offset: Position from which search results will be presented
        :param nsfw: boolean enabling/disabling nsfw filter

        :returns: list of queries matching search keyword
        :rtype: PagedResult
        """
        if nsfw is None:
            nsfw = self.nsfw
        uri = 'manga'
        params = {
            "q": keyword,
            "limit": limit,
            'offset': offset,
            "fields": fields.to_payload(),
            'nsfw': nsfw
        }
        temp = self._api_handler.call(uri, params=params)
        r_class = Node if fields == Fields.node() else MangaObject
        return PagedResult([r_class(**manga) for manga in temp["data"]], temp['paging'])

    def get_manga_details(self, manga_id: int):
        """
        Get full info about manga with provided id

        :param int manga_id: id on https://myanimelist.net

        :returns: MangaObject for requested id
        :rtype: MangaObject
        """
        uri = f'manga/{manga_id}'
        params = {"fields": Fields.manga().to_payload()}
        data = self._api_handler.call(uri, params=params)
        return MangaObject(**data)

    def get_manga_fields(self, manga_id: int, fields: Fields) -> MangaObject:
        """

        Get specific fields from MAL manga entry with provided id

        :param int manga_id: id on https://myanimelist.net
        :param Fields fields: Fields that will be returned with manga object

        :returns: MangaObject for requested id
        :rtype: MangaObject
        """
        uri = f'anime/{manga_id}'
        params = {'fields': fields.to_payload()}
        data = self._api_handler.call(uri, params=params)
        return MangaObject(**data)

    def get_manga_ranking(self, ranking_type: Union[str, MangaRankingType] = MangaRankingType.MANGA, fields: Fields = Fields.manga(), limit: int = 20, offset: int = 0) -> Union[PagedResult[Node], PagedResult[MangaObject]]:
        """

        Get current manga ranking from MAL

        :param MangaRankingType ranking_type: type of manga ranking that will be fetched from API, refer to MangaRankingType dataclass for more info
        :param Fields fields: Fields that will be returned additionally with manga data
        :param int limit: number of queries returned
        :param int offset: Position from which search results will be presented

        :returns: List of queries with pagination support
        :rtype: PagedResult
        """
        uri = 'manga/ranking'

        if isinstance(ranking_type, str):
            try:
                ranking_type = MangaRankingType(ranking_type)
            except ValueError:
                raise ValueError(f"ranking_type can't be '{ranking_type}'")

        params = {
            "ranking_type": ranking_type,
            "limit": limit,
            "fields": fields.to_payload(),
            'offset': offset,
        }
        temp = self._api_handler.call(uri, params=params)
        r_class = Node if fields == Fields.node() else MangaObject
        return PagedResult([r_class(**manga) for manga in temp["data"]], temp['paging'])
