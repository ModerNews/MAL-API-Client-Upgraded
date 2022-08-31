Changelog
=========

Version 1.2
~~~~~~~~~~~
* Reworked models:
    * Added new enum for Seasons
    * Added enum for Seasonal Anime Sorting
    * Added enums for Anime and Manga ranking sorting
    * Added enums for Manga and Anime list sorting
* New Classes for fields management: `Fields`, `AuthorsFields`, `ListStatusFields`
* Changed syntax for multiple methods:
    * `Client.search_anime`
    * `Client.search_manga`
    * `Client.get_manga_ranking`
* Added new methods for fields interaction:
    * `Client.get_anime_fields`
    * `Client.get_manga_fields`
* Updated documentation

Version 1.1
~~~~~~~~~~~
* Introducing Sphinx documentation
* Renamed multiple functions
    * `Client.update_anime_my_list_status` to `Client.update_my_anime_list_status`
    * `Client.delete_anime_list_status` to `Client.delete_my_anime_list_status`
    * `Client.update_manga_my_list_status` to `Client.update_my_manga_list_status`
    * `Client.delete_manga_list_status` to `Client.delete_my_manga_list_status`
* Get fully rid of json_serializer.py
* Fixed Exceptions and Models not hinting
* Fixed `Client.refresh_bearer_token` not working

Version 1.0
~~~~~~~~~~~
* New function `generate_token` used for generating access token (as it`s complicated task for user)
* `get_anime`, `search_anime`, `get_manga` and `search_manga` now return pydantic models instead of JSON dictionaries or ResponseJSON helper class
* Introducing multiple new pydantic models in models.py: `Genre`, `Asset`, `Nsfw`, `Broadcast`, `Node`, `Relation`, `RelationType`, `AnimeListStatus`, `Rating`, `Recommendation`, `Season`, `Studio`, `Author`, `MyAnimeListStatus`, `AnimeType`, `AnimeStatus`, `Source`, `AnimeObject`, `MyMangaListStatus`, `MangaType`, `MangaStatus`, `MangaObject`
* Introducing global and local variable nsfw determining if nsfw filter is either enabled or disabled during querying
* Introducing new exceptions for HTTP errors: 400, 401, 403 and 404 to simplify exception handling
* All functions in anime.py and manga.py are now type hinted
* All rewritten functions now have in-python documentation, works on sphinx documentation are started
* Updated README.md to match new package data
* Changed setup.py to match new package data
* Introduction of requirements.txt and pyproject.toml to control dependencies and builds