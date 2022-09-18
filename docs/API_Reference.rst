API Reference
==============

.. _Client:

Base Class
~~~~~~~~~~

.. py:currentmodule:: malclient

.. autoclass:: Client

.. automethod:: Client.get_user_info


Anime-related functions
~~~~~~~~~~~~~~~~~~~~~~~

.. py:currentmodule:: malclient

.. automethod:: Client.get_anime_details

.. automethod:: Client.get_anime_fields

.. automethod:: Client.search_anime

.. automethod:: Client.get_anime_ranking

.. automethod:: Client.get_seasonal_anime

.. automethod:: Client.get_suggested_anime


Manga-related functions
~~~~~~~~~~~~~~~~~~~~~~~

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

.. py:currentmodule:: malclient

.. automethod:: Client.update_my_anime_list_status

.. automethod:: Client.delete_my_anime_list_status

.. automethod:: Client.get_user_anime_list

.. automethod:: Client.update_my_manga_list_status

.. automethod:: Client.delete_my_manga_list_status

.. automethod:: Client.get_user_manga_list


Utility
~~~~~~~

.. py:currentmodule:: malclient

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
