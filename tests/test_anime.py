import json
from sqlite3 import SQLITE_SAVEPOINT
from unittest import mock

import malclient
import pytest

from malclient.Datamodels import Season, Fields, SeasonalAnimeSorting
# from malclient.anime import __anime_fields__

ANIME_RESPONSE = {
    "id": 1,
    "title": "anime title",
    "main_picture": {"medium": "https://url/1", "large": "https://url/2"},
    "alternative_titles": {"synonyms": ["another title"], "en": "", "ja": "別の名前"},
    "start_date": "2022-07-20",
    "end_date": "2022-07-20",
    "synopsis": "synopsis",
    "mean": "3.2",
    "rank": 345,
    "popularity": 10,
    "num_list_users": 10,
    "average_episode_duration": 2400,
    "my_list_status": {
        "status": "plan_to_watch",
        "score": 0,
        "num_episodes_watched": 0,
        "is_rewatching": False,
        "updated_at": "2022-04-03T22:48:25+00:00",
    },
    "broadcast": {"day_of_the_week": "saturday", "start_time": "23:30"},
    "num_scoring_users": 3,
    "rating": "pg_13",
    "nsfw": "white",
    "created_at": "2021-08-08T15:50:11+00:00",
    "updated_at": "2022-03-31T08:40:54+00:00",
    "media_type": "ona",
    "status": "not_yet_aired",
    "genres": [{"id": 1, "name": "Action"}],
    "num_episodes": 0,
    "start_season": {"year": 2022, "season": "summer"},
    "source": "novel",
    "studios": [{"id": 1, "name": "a studio"}],
}


def mocked_client(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.data = json_data["data"]
            self.paging = json_data["paging"]
            self.status_code = status_code

        def __getitem__(self, item):
            return getattr(self, item)

        def json(self):
            return self.json_data

    if "anime/season" in kwargs["uri"]:
        return MockResponse(
            {"data": [ANIME_RESPONSE], "paging": {"next": "https://mock-next"}}, 200
        )

    return MockResponse(None, 404)


@pytest.fixture
def client():
    return malclient.Client(access_token="a_random_token", nsfw=True)


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_season_fail(self, client):
    with pytest.raises(ValueError):
        response = client.get_seasonal_anime("summmer", 2022, limit=1)


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_fields(self, client):
    response = client.get_seasonal_anime("summer", 2022, limit=1)
    for field in Fields.anime().to_payload().split(','):
        if field not in [
            "pictures",
            "background",
            "related_anime",
            "related_manga",
            "recommendations",
        ]:
            assert field in response[0]


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_season_str_success(self, client):
    response = client.get_seasonal_anime("summer", 2022, limit=1)
    assert response == [ANIME_RESPONSE]


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_season_obj_success(self, client):
    response = client.get_seasonal_anime(Season.SUMMER, 2022, limit=1)
    assert response == [ANIME_RESPONSE]


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_sort_str_fail(self, client):
    with pytest.raises(ValueError):
        response = client.get_seasonal_anime(Season.SUMMER, 2022, sort="anime", limit=1)


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_sort_obj_success(self, client):
    response = client.get_seasonal_anime(
        Season.SUMMER, 2022, sort="anime_score", limit=1
    )
    assert response == [ANIME_RESPONSE]


@mock.patch("malclient.request_handler.APICaller.call", side_effect=mocked_client)
def test_get_seasonal_anime_sort_obj_success(self, client):
    response = client.get_seasonal_anime(
        Season.SUMMER, 2022, sort=SeasonalAnimeSorting.USER_NUM, limit=1
    )
    assert response == [ANIME_RESPONSE]
