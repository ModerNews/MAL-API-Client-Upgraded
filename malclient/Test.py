import malclient
from objects import AnimeObject
from dotenv import load_dotenv
import os

load_dotenv()
_mal_access = os.getenv('mal_access_token')
_mal_client = os.getenv('mal_client')
_mal_cient_secret = os.getenv('mal_client_secret')
_mal_refresh = os.getenv('mal_refresh')

client = malclient.Client()
client.init(access_token=_mal_access)

# client.refresh_bearer_token(_mal_client, _mal_cient_secret, _mal_refresh)

anime = client.get_anime_details(42361)
anime = AnimeObject(anime.d)

input('Enter to stop...')