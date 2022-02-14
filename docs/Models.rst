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

.. autoclass:: Rating

.. autopydantic_model:: Season

.. autoenum:: Source
    :members:

.. autopydantic_model:: Studio


Manga Specific
~~~~~~~~~~~~~~

.. autopydantic_model:: MangaObject

.. autoclass:: MangaType

.. autopydantic_model:: MyMangaListStatus

.. autoenum:: MangaStatus 