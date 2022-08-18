API Reference
==============

.. _Client:

Base Class
~~~~~~~~~~

.. py:currentmodule:: malclient

.. autoclass:: Client


Anime-related functions
~~~~~~~~~~~~~~~~~~~~~~~

Already finished:

.. py:currentmodule:: malclient

.. automethod:: Client.get_anime_details

.. automethod:: Client.get_anime_fields

.. automethod:: Client.search_anime

.. automethod:: Client.get_anime_ranking

.. automethod:: Client.get_seasonal_anime

.. automethod:: Client.get_suggested_anime


Manga-related functions
~~~~~~~~~~~~~~~~~~~~~~~

Already finished:

.. py:currentmodule:: malclient

.. automethod:: Client.get_manga_details

.. automethod:: Client.get_manga_fields

.. automethod:: Client.search_manga

.. automethod:: Client.get_manga_ranking


Forum Boards
~~~~~~~~~~~~

Forum boards stay pretty much untouch, either by me or previous developer, so there is nothing available at the moment
I will be working on bringing it back though.


User List
~~~~~~~~~~

I looked through it, manga nad anime list are available in API, but they need to be rewritten


Utility
~~~~~~~

.. py:currentmodule:: malclient

.. automethod:: Client.get_user_info

.. autoclass:: PagedResult
    :members:


Exceptions
~~~~~~~~~~

.. py:currentmodule:: malclient

.. autoexception:: APIException

.. autoexception:: BadRequest

.. autoexception:: Unauthorized

.. autoexception:: Forbidden

.. autoexception:: NotFound
