Data Models
===========

Universal
~~~~~~~~~

.. py:currentmodule:: malclient

.. autopydantic_model:: Node

.. autopydantic_model:: Asset

.. autopydantic_model:: Genre

.. autopydantic_model:: Relation

.. autoenum:: RelationType
    :members:

.. autoenum:: Nsfw
    :members:

.. autopydantic_model:: Recommendation


Anime Specific
~~~~~~~~~~~~~~

.. autopydantic_model:: AnimeObject

.. autoenum:: AnimeStatus
    :members:

.. autoclass:: AnimeType

.. autopydantic_model:: Broadcast

.. autopydantic_model:: MyAnimeListStatus

.. autopydantic_model:: Statistics

.. autoclass:: Rating

.. autopydantic_model:: AnimeSeason

.. autoenum:: Season
    :members:

.. autoenum:: AnimeSource
    :members:

.. autopydantic_model:: Studio

.. autoenum:: AnimeRankingType
    :members:

.. autoenum:: SeasonalAnimeSorting
    :members:

.. autoenum:: MyAnimeListSorting
    :members:


Manga Specific
~~~~~~~~~~~~~~

.. autopydantic_model:: MangaObject

.. autoclass:: MangaType

.. autopydantic_model:: MyMangaListStatus

.. autoenum:: MangaStatus
    :members:

.. autoenum:: MangaRankingType
    :members:

.. autoenum:: MyMangaListSorting
    :members:

Fields
~~~~~~

.. autoclass:: Fields
    :members:

    .. list-table:: Available Fields
        :widths: 25 50
        :header-rows: 1

        * - Value
          - Description
        * - id
          - Unique ID from `MyAnimeList <https://myanimelist.net>`_
        * - title
          - Name of the show
        * - main_picture
          - Picture picked to represent series
        * - alternative_titles
          - Synonyms and translations of title
        * - start_date
          - start date
        * - end_date
          - finish date
        * - synopsis
          - Short description of series
        * - background
          - | Additional information about show
            | You cannot contain this field in a list
        * - mean
          - | Average of all scores
            | Sometimes, f.e. when number of users is low, mean won't be calculated
        * - rank
          - | Position in ranking on website
            | Sometimes, f.e. when number of users is low, rank won't be calculated
        * - popularity
          - Position in popularity ranking on website
        * - num_list_users
          - Number of users who have this title in their lists
        * - num_scoring_users
          - Number of users who have give score to this title
        * - updated_at
          - Date and time of last update
        * - genres
          - List of all genres assigned to this title
        * - my_list_status
          - Entry from validated user list for this title
        * - pictures
          - | List containing all assets
            | You cannot contain this field in a list.
        * - related_anime
          - | List of all related anime
            | Currently not working for manga entries
            | You cannot contain this field in a list.
        * - related_manga
          - | List of all related manga
            | Currently not working for anime entries
            | You cannot contain this field in a list.
        * - recommendations
          - | Summary of recommended titles for people who liked this o
            | You cannot contain this field in a list.
        * - nsfw
          - NSFW rating value
        * - created_at
          - Creation date for this entry
        * - media_type
          - Media type
        * - status
          - Current airing status
        * - num_favorites
          - Number of users who have this title in their favourites
        * - num_episodes
          - | Total number of episodes
            | Available only for anime entries
        * - start_season
          - | Season in which anime started airing
            | Available only for anime entries
        * - broadcast
          - | Day of broadcast
            | Available only for anime entries
        * - source
          - | Media type for anime source
            | Available only for anime entries
        * - average_episode_duration
          - | Avarage length of one episode
            | Available only for anime entries
        * - rating
          - | TV age rating
            | Available only for anime entries
        * - studios
          - | list of studios creating this anime
            | Available only for anime entries
        * - opening_theme
          - | List of opening songs
            | Available only for anime entries
        * - ending_theme
          - | List of ending songs
            | Available only for anime entries
        * - statistics
          - | Number of users for each list status
            | Available only for anime entries
            | You cannot contain this field in a list.
        * - num_volumes
          - | Total number of volumes for this manga
            | Available only for manga entries
        * - num_chapters
          - | Total number of chapters for this manga
            | Available only for manga entries
        * - authors
          - | List of people who created this manga
            | Available only for manga entries
        * - serialization
          - | Information on manga serialization
            | Available only for manga entries
            | You cannot contain this field in a list.


.. autoclass:: AuthorFields
    :members:

    .. list-table:: Available Fields
        :widths: 25 50
        :header-rows: 1

        * - Value
          - Description
        * - first_name
          - Author's first name
        * - last_name
          - Author's last name


.. autoclass:: ListStatusFields
    :members:

    .. list-table:: Available Fields
        :widths: 25 50
        :header-rows: 1

        * - score
          - Number of points given
        * - status
          - Status on list
        * - updated_at
          - Date and time of last update
        * - start_date
          - Start date
        * - finish_date
          - Finish Date
        * - priority
          - Importance, set by user
        * - tags
          - Tags given to this entry by user
        * - comments
          - Additional comment provided by user
        * - num_episodes_watched
          - | Number of episodes watched by user
            | Available only for anime entries
        * - is_rewatching
          - | Describes if user is rewatching this series
            | Available only for anime entries
        * - num_times_rewatched
          - | Number of times user already rewatched this series
            | Available only for anime entries
        * - rewatch_value
          - | How likely is user to rewatch this series
            | Available only for anime entries
        * - is_rereading
          - | Describes if user is rewatching this series
            | Available only for manga entries
        * - num_volumes_read
          - | Number of volumes read by user
            | Available only for anime entries
        * - num_chapters_read
          - | Number of chapters read by user
            | Available only for anime entries
        * - num_times_reread
          - | Number of times user already reread this series
            | Available only for manga entries
        * - reread_value
          - | How likely is user to reread this series
            | Available only for manga entries