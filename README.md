# MAL-API-Client-Upgraded

![PyPI](https://img.shields.io/pypi/v/malclient-upgraded?logo=myanimelist&style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/malclient-upgraded?logo=python&logoColor=%23ffd43b&style=for-the-badge)
![PyPI - License](https://img.shields.io/pypi/l/malclient-upgraded?style=for-the-badge&color=3EB049) </br>
![Read the Docs](https://img.shields.io/readthedocs/mal-api-client-upgraded?style=for-the-badge&color=3EB049)
![PyPI - Downloads](https://img.shields.io/pypi/dm/malclient-upgraded?style=for-the-badge&color=3EB049) </br>
A third party object-oriented python3 client library for MyAnimeList's official REST API.
Originally created by [@JFryy](https://github.com/JFryy/MAL-API-Client), dropped around 2 years ago, picked up and rewritten by ModerNews to fit more modern standards and new REST API functions.

## Documentation
Unsure what to do? [Check out our documentation](https://mal-api-client-upgraded.readthedocs.io) </br>

## Installation
**Python 3.9 or newer required**, this is due to changes in type hinting guidelines, for more info regarding this issue read [PEP 585](https://peps.python.org/pep-0585/)  
Install the latest stable version from [PyPI](https://pypi.org/project/malclient-upgraded/)  
`pip install malclient-upgraded`  

Or current unstable version directly from GitHub:  
`pip install git+https://github.com/ModerNews/MAL-API-Client-Upgraded`


## Authentication
Client library uses OAuth2 authorization, all you need to do is register your app [here](https://myanimelist.net/apiconfig).
Main auth requires access token:

```python
import malclient

malclient.client(access_token=token)
```

Alternatively can authenticate using your client ID

```python
import malclient

malclient.client(client_id=id)
```

You can generate token old-fashioned way using [this tutorial](https://myanimelist.net/blog.php?eid=835707)  
Or you can use function implemented in API

```python
import malclient

print(malclient.generate_token("<YOUR_CLIENT_ID>", "<YOUR_CLIENT_SECRET>"))
```

Although remember to call it only once and, then use the token generated this way, optionally with `Client.refresh_bearer_token` method  

As mentioned previously, if you're scared that your token will time out you can also utilize `Client.refresh_bearer_token` function

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
- [ ] Implement people endpoint
- [ ] Implement episodes endpoint
- [ ] Implement additional search endpoint

### Useful resources
- [MAL auth guide](https://myanimelist.net/blog.php?eid=835707)
- [Unofficial API Discord](https://discord.gg/XqzqDkzuFx)
- [Official MAL API Club](https://myanimelist.net/clubs.php?cid=13727)

## P.S. 
If anything bugs you, you can always reach me out at discord Gruzin#0911 as well
