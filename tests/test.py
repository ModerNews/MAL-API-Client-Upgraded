import malclient
import os

client = malclient.Client(access_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY2OTllNDU2YjQzOWFiZDNhY2E0NTA3ZTQzMDI0NzY5YTEwMjM2MjlkNjFkYzVhNjg1MGY1NWVhNDgxODM0NDk0NGEzZWZkZDhlNWMyYTExIn0.eyJhdWQiOiI0ODU2M2I5MDYzMTBkM2ZkYjRjZWZhMWMxODc3YmZjMyIsImp0aSI6IjY2OTllNDU2YjQzOWFiZDNhY2E0NTA3ZTQzMDI0NzY5YTEwMjM2MjlkNjFkYzVhNjg1MGY1NWVhNDgxODM0NDk0NGEzZWZkZDhlNWMyYTExIiwiaWF0IjoxNjg1MDUzMDk3LCJuYmYiOjE2ODUwNTMwOTcsImV4cCI6MTY4NzczMTQ5Nywic3ViIjoiMTA4MzEzMzAiLCJzY29wZXMiOltdfQ.JNwimqA6JRY8ZVaHjWKdj7lbW7Ydcb8SHLksYiONBw02XIYmA6aoWyqENDM0ZYwnBJEdB77bd5UZpmm-BEGtS-GwRalzBovgoA7DWviP5ee1R3NdCr_xXXcOsQiVfPr5CWq5vEourWnXI4sYu3zH24fmkZYPpi0fdU1PPvowNc0d3JlRjMKTVsI2AdTB-sqvHLSQLGhC11ZSi_Ycq02BRwkqd_7mkYnA_tWVJOyVRKeuu00DV1d0aNfVAqUcLc60vWBrG96DBlhiPfEESzxVJ6r_nr4KNPvtR3FoOI35Wxj_q5f2A4b6BUxEbv1Rh8czSzDv_jxE_kHPUDMDLre2MQ",
                          refresh_token=os.getenv("refresh_token"))

fields = malclient.Fields.all()

anime1 = client.search_anime('Fate')
anime2 = client.get_anime_fields(10087, fields=fields)
anime3 = client.get_anime_ranking(ranking_type='bypopularity', fields=fields)
anime4 = client.get_user_anime_list('michalwrpo', status='completed')
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

character1 = client.get_character_details(161357)
character2 = client.get_anime_characters(21)

person1 = client.get_person_details(160, fields=malclient.PersonFields.all())
print('Ready to finish...')