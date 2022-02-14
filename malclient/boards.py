class Boards():

    def __init__(self):
        return

    def get_forum_boards(self):
        uri = 'forum/boards'
        return self._api_handler.call(uri)

    def get_forum_topic_detail(self, topic_id, limit=100):
        uri = f'forum/topic/{topic_id}'
        params = {'limit': limit}
        return self._api_handler.call(uri, params=params)


#    TODO:
#    def get_forum_topics
