import malclient
import os

client = malclient.Client(access_token=os.getenv("access_token"),
                          refresh_token=os.getenv("refresh_token"))

fields = malclient.Fields.all()

anime1 = client.search_anime('Fate')
anime2 = client.get_anime_fields(10087, fields=fields)
anime3 = client.get_anime_ranking(ranking_type='bypopularity', fields=fields)
anime4 = client.get_user_anime_list('michalwrpo')
anime5 = client.get_user_anime_list('Rafist0', status='completed', fields=fields, list_status_fields=malclient.ListStatusFields.all())
anime6 = client.get_seasonal_anime('winter', 2022)
anime7 = client.get_suggested_anime()

forum1 = client.get_forum_boards()
forum2 = client.get_forum_topics(board_id=5)
forum3 = client.get_forum_topic_detail(topic_id=2058371)

manga1 = client.search_manga('Kaguya')
manga2 = client.get_manga_details(127084)
manga3 = client.get_manga_ranking(ranking_type=malclient.MangaRankingType.FAVORITE, fields=fields)
manga4 = client.get_user_manga_list('michalwrpo')
print('Ready to finish...')