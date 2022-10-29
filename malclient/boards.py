from typing import Literal

from .Datamodels import ForumCategory, ForumTopicDetail, ForumTopic
from .Datamodels import PagedResult


class Boards:
    def __init__(self):
        return

    def get_forum_boards(self):
        """

        Get list of forum boards from MAL

        :returns: List containing all forum boards on MAL
        :rtype: list[ForumCategory]
        """
        uri = 'forum/boards'
        return [ForumCategory(**data) for data in self._api_handler.call(uri)['categories']]
        # return self._api_handler.call(uri)

    def get_forum_topic_detail(self, topic_id: int, *, limit: int = 100, offset: int = 0):
        """
        Get details about forum topic from MAL

        :param int topic_id: id of topic for which data will be fetched
        :param int limit: number of posts in topic to fetch
        :param int offset: number of posts in topic from start to be skipped
        :returns: Details about forum topic
        :rtype: ForumTopicDetail
        """
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
                         query: str = None,
                         topic_user_name: str = None,
                         user_name: str = None):
        """

        Get list of topics available on MAL, by board_id, subboard_id, query, topic_user_name or user_name
        Descriptions of parameters are uncertain as they're missing in official API documentation

        :param int board_id: id of board wanted topics are on
        :param int subboard_id: id of subboard wanted topics are on
        :param str query: query by which forum topics will be filtered by
        :param str topic_user_name: topics created by user with this name
        :param str user_name: topic in which user with this username took part
        :param int limit: number of topics to fetch
        :param int offset: number of topics from start to be skipped
        :param str sort: sorting method, currently only `recent` is available
        :returns: List of forum topics matching provided parameters
        :rtype: PagedResult[ForumTopic]
        """
        if not(query or board_id or subboard_id or topic_user_name or user_name):
            raise AttributeError("You need to provide one of those: q, board_id, subboard_id, topic_user_name, user_name")
        uri = 'forum/topics'
        params = {'board_id': board_id,
                  'subboard_id': subboard_id,
                  'limit': limit,
                  'offset': offset,
                  'sort': sort,
                  'q': query,
                  'topic_user_name': topic_user_name,
                  'user_name': user_name}
        temp = self._api_handler.call(uri, params=params)
        return PagedResult([ForumTopic(**topic) for topic in temp['data']], temp['paging'])