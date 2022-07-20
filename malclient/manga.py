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

        :param keyword: string to look by
        :param limit: number of queries returned
        :param nsfw: boolean enabling/disabling nsfw filter

        :returns: list of manga Node objects
        :rtype: list[Node]
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

        :param id: id on https://myanimelist.net

        :returns: MangaObject for requested id
        :rtype: MangaObject
        """
        uri = f'manga/{manga_id}'
        params = {"fields": Fields.manga().to_payload()}
        data = self._api_handler.call(uri, params=params)
        return MangaObject(**data)

    def get_manga_fields(self, id: int, fields: Fields) -> MangaObject:
        """

        Get specific fields from MAL manga entry with provided id

        :param int id: id on https://myanimelist.net
        :param list[str] fields: list of string field names
        :returns: MangaObject for requested id
        :rtype: MangaObject
        """
        uri = f'anime/{id}'
        params = {'fields': fields.to_payload()}
        data = self._api_handler.call(uri, params=params)
        return MangaObject(**data)

    def get_manga_ranking(self, ranking_type: Union[str, MangaRankingType] = MangaRankingType.MANGA, fields: Fields = Fields.manga(), limit=20) -> Union[PagedResult[Node], PagedResult[MangaObject]]:
        uri = 'manga/ranking'

        if isinstance(ranking_type, str):
            try:
                ranking_type = MangaRankingType(ranking_type)
            except ValueError:
                raise ValueError(f"ranking_type can't be '{ranking_type}'")

        params = {
            "ranking_type": ranking_type,
            "limit": limit,
            "fields": fields.to_payload()
        }
        temp = self._api_handler.call(uri, params=params)
        r_class = Node if fields == Fields.node() else MangaObject
        return PagedResult([r_class(**manga) for manga in temp["data"]], temp['paging'])
