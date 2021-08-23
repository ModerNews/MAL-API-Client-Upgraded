from objects import MangaObject, Node

class Manga():

    def __init__():
        return

    def search_manga(self, query, limit=20, nsfw=None):
        uri = 'manga'
        params = {
            "q": query,
            "limit": limit,
            "fields": ','.join(self.manga_fields),
            'nsfw': True if nsfw is True else False
        }
        return [Node(list(temp_object.values())) for temp_object in self._api_handler.call(uri, params=params)]

    def get_manga_details(self, manga_id):
        uri = f'manga/{manga_id}'
        params = {"fields": ','.join(self.manga_fields)}
        return MangaObject(self._api_handler.call(uri, params=params))

    # TODO objectify manga ranking
    def get_manga_ranking(self, ranking_type="manga", limit=20):
        uri = 'manga/ranking'
        ranking_types = [
            "novels", "oneshots", "doujin", "manhwa", "manhua", "bypopularity",
            "favorite"
        ]

        if ranking_type not in ranking_types:
            return
        params = {
            "ranking_type": ranking_type,
            "limit": limit,
            "fields": ','.join(self.manga_fields)
        }
        return self._api_handler.call(uri, params)
