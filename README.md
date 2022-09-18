# MAL-API-Client-Upgraded
A third party object-oriented python3 client library for MyAnimeList's official REST API.
Originally created by [@JFryy](https://github.com/JFryy/MAL-API-Client), dropped around 2 years ago, picked up and rewritten by ModerNews to fit more modern standards and new REST API functions.

## Documentation
There is first version of docs available, [check it out](https://mal-api-client-upgraded.readthedocs.io)

## Installation
**Python 3.9 or newer required**, this is due to changes in type hinting guidelines, for more info regarding this issue read [PEP 585](https://peps.python.org/pep-0585/)  
Install the latest stable version from [PyPI](https://pypi.org/project/malclient-upgraded/)  
`pip install malclient-upgraded`  

Or current unstable version directly from GitHub:  
`pip install git+https://github.com/ModerNews/MAL-API-Client-Upgraded`


## Authentication
Client library uses OAuth2 authorization, all you need to do is register your app [here](https://myanimelist.net/apiconfig), and generate access token.  
You can do it old-fashioned way using [this tutorial](https://myanimelist.net/blog.php?eid=835707)  
Or you can use function implemented in API
```python
import malclient

print(malclient.generate_token("<YOUR_CLIENT_ID>", "<YOUR_CLIENT_SECRET>"))
```

Although remember to call it only once and, then use the token generated this way, optionally with `Client.refresh_bearer_token` method  
Once an access token is retrieved, you can simply authenticate with this api with the following:
```python
import malclient

client = malclient.Client(access_token="<YOUR_ACCESS_TOKEN>")
```

As mentioned previously, if your scared that your token will time out you can also utilize `Client.refresh_bearer_token` function
```python
client.refresh_bearer_token(
          client_id="<your-client-id>",
          client_secret="<your-client-secret>",
          refresh_token="<your-refresh-token>")
```

For any other issues regarding authentication, [please refer to the following guide](https://myanimelist.net/blog.php?eid=835707).

## Quick Start Examples
I contained some examples of usage of this wrapper, note that all responses are converted to python objects using pydantic

```python
import malclient

# nsfw filter is enabled by default, although it's recommended to disable it if your results are missing titles, 
#  you can also enable/disable it for every query individually 
client = malclient.Client(access_token="<your-access-token>", nsfw=True)

# search anime, returns list
anime = client.search_anime("cowboy", limit=20)
for item in anime:
    # prints only titles
    print(item)
    # prints all attributes of object
    print(repr(item))
    
# search anime, returns list
manga = client.search_manga("Monogatari", limit=20)
for item in manga:
    # prints only titles
    print(manga)
    # prints all attributes of object
    print(repr(manga))

# Get individual anime by ID
anime = client.get_anime_details(1)
print(anime)
print(repr(anime))

# Update anime List based off of search results
anime = client.search_anime("Monogatari", limit=1)
```

### Most Imoprtant To-Do's
- [ ] Rewrite boards (currently disabled)
- [ ] Rewrite my list updaters

## P.S. 
If anything bugs you, you can always reach me out at discord Gruzin#0911 as well
