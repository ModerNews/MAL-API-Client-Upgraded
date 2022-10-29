.. _Inconsistencies:

===============
Inconsistencies
===============
.. warning::
    | Take note that what I described underneath are only mine and other peoples findings - they might not contain full information or be outdated
    | Special thanks to MAL Forums users Skylake, Uchuu, DiamondTMZ, KasuteDev and others for providing those informations

| Unfortunately official API docs contain multiple mistakes and inconsistencies, of course they account for what is available in wrapper.
    If you'll find out about something that's not documented and not published in wrapper please let me know:
| **Discord:** Gruzin#0911
| **MAL Forums:** `Official api feed <https://myanimelist.net/forum/?topicid=2006357>`_

MangaType
=========

**MangaType** enum has additional value `light_novel` not mentioned in docs,
example entries:

.. collapse:: MangaType Example

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/manga/74697?fields=id,title,main_picture,author,media_type

    .. code-block:: json

        {
            "id": 74697,
            "title": "Re:Zero kara Hajimeru Isekai Seikatsu",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/manga/1/129447.jpg",
                "large": "https://api-cdn.myanimelist.net/images/manga/1/129447l.jpg"
            },
            "media_type": "light_novel"
        }

AnimeSource
===========

**AnimeSource** enum, representing source field for anime can have values `web_novel`, `mixed_media`, examples:

.. collapse:: AnimeSource Example

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/anime/48556?fields=source

    .. code-block:: json

        {
            "id": 48556,
            "title": "Takt Op. Destiny",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/anime/1449/117797.jpg",
                "large": "https://api-cdn.myanimelist.net/images/anime/1449/117797l.jpg"
            },
            "source": "mixed_media"
        }

MangaStatus
===========

**MangaStatus** enum, representing status field for manga entries can take `on_hiatus` or `discontinued` as values.

.. collapse:: MangaStatus Examples

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/manga/656?fields=status

    .. code-block:: json

        {
            "id": 656,
            "title": "Vagabond",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/manga/1/259070.jpg",
                "large": "https://api-cdn.myanimelist.net/images/manga/1/259070l.jpg"
            },
            "status": "on_hiatus"
        }

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/manga/669?fields=status

    .. code-block:: json

        {
            "id": 669,
            "title": "Highschool of the Dead",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/manga/2/188884.jpg",
                "large": "https://api-cdn.myanimelist.net/images/manga/2/188884l.jpg"
            },
            "status": "discontinued"
        }

OP and ED Themes
================

Anime queries take `opening_themes` and `ending_themes` as possible field parameters, not present in docs.

.. collapse:: Themes Example

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/anime/48556?fields=source,opening_themes,ending_themes

    .. code-block:: json

        {
            "id": 48556,
            "title": "Takt Op. Destiny",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/anime/1449/117797.jpg",
                "large": "https://api-cdn.myanimelist.net/images/anime/1449/117797l.jpg"
            },
            "source": "mixed_media",
            "opening_themes": [
                {
                    "id": 71568,
                    "anime_id": 48556,
                    "text": "\"takt (タクト)\" by ryo (supercell) feat. Mafumafu, gaku"
                }
            ],
            "ending_themes": [
                {
                    "id": 71567,
                    "anime_id": 48556,
                    "text": "\"SYMPHONIA\" by Mika Nakashima"
                }
            ]
        }

Broken Relations
================

You cannot fetch `related_manga` for `Client.get_anime_details()` and `Client.get_anime_fields()` functions, despite being documented, they are non-existent in practice.
Same thing goes for `related_anime` field in `Client.get_manga_details()` and `Client.get_manga_fields()`.

Sorting by ID
=============

For **MyAnimeListSorting** and **MyMangaListSorting** enums value `ID` is disabled, despite being present in documentation, trying to sort with it raises `400 Bad Request` Error.

Number Favorites
================

Anime and manga endpoints take additional fields parameter `num_favorites` which isn't mentioned in docs

.. collapse:: `num_favourites` Example

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/anime/48556?fields=num_favorites

    .. code-block:: json

        {
            "id": 48556,
            "title": "Takt Op. Destiny",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/anime/1449/117797.jpg",
                "large": "https://api-cdn.myanimelist.net/images/anime/1449/117797l.jpg"
            },
            "num_favorites": 4364
        }

    .. code-block:: bash

        curl GET https://api.myanimelist.net/v2/manga/669?fields=num_favorites

    .. code-block:: json

        {
            "id": 669,
            "title": "Highschool of the Dead",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/manga/2/188884.jpg",
                "large": "https://api-cdn.myanimelist.net/images/manga/2/188884l.jpg"
            },
            "num_favorites": 3002
        }

Relation Types
==============

**RelationType** enum, representing `related_anime.relation_type` or `related_manga.relation_type`, takes values not mentioned in docs: `spin_off` and `character`

.. collapse:: RelationType Examples

    .. note::
        Please note that in order to keep readability following response was trimmed to contain important data only

    .. code-block:: bash

        curl GET

    .. code-block:: json

        {
            "id": 10087,
            "title": "Fate/Zero",
            "main_picture": {
                "medium": "https://api-cdn.myanimelist.net/images/anime/1887/117644.jpg",
                "large": "https://api-cdn.myanimelist.net/images/anime/1887/117644l.jpg"
            },
            "related_anime": [
                {
                    "node": {
                        "id": 38936,
                        "title": "Lord El-Melloi II Sei no Jikenbo: Rail Zeppelin Grace Note - Hakamori to Neko to Majutsushi",
                        "main_picture": {
                            "medium": "https://api-cdn.myanimelist.net/images/anime/1762/114436.jpg",
                            "large": "https://api-cdn.myanimelist.net/images/anime/1762/114436l.jpg"
                        }
                    },
                    "relation_type": "character",
                    "relation_type_formatted": "Character"
                },
            ]
        }

