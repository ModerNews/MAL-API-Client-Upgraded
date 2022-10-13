class Boards:

    def __init__(self):
        return

    def get_forum_boards(self):
        uri = 'forum/boards'
        return [ForumCategory(**data) for data in self._api_handler.call(uri)['categories']]
        # return self._api_handler.call(uri)

    def get_forum_topic_detail(self, topic_id: int, *, limit: int = 100, offset: int = 0):
        uri = f'forum/topic/{topic_id}'
        params = {'limit': limit,
                  'offstet': offset}
        temp = self._api_handler.call(uri, params=params)
        return ForumTopicDetail(paging_data=temp['paging'], **temp["data"])

    def get_forum_topics(self, *,
                         board_id: int = None,
                         subboard_id: int = None,
                         limit: int = 100,
                         offset: int = 0,
                         sort: Literal["recent"] = "recent",
                         q: str = None,
                         topic_user_name: str = None,
                         user_name: str = None):
        if not(q or board_id or subboard_id or topic_user_name or user_name):
            raise AttributeError("You need to provide one of those: q, board_id, subboard_id, topic_user_name, user_name")
        uri = f'forum/topics'
        params = {'board_id': board_id,
                  'subboard_id': subboard_id,
                  'limit': limit,
                  'offset': offset,
                  'sort': sort,
                  'q': q,
                  'topic_user_name': topic_user_name,
                  'user_name': user_name}
        temp = self._api_handler.call(uri, params=params)
        return PagedResult([ForumTopic(**topic) for topic in temp['data']], temp['paging'])